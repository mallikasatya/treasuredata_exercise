import argparse
import os
import tdclient
import time
import datetime
import sys
import unicodedata

from prettytable import PrettyTable

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--column", dest="col_list", nargs='+', type=str)
parser.add_argument("-m", "--min", dest="min_time",type=long)
parser.add_argument("-M", "--max", dest="max_time",type=long)
parser.add_argument("-e", "--engine", dest="engine",nargs='?',default='presto',choices=['hive','presto'])
parser.add_argument("-f", "--format", dest="format",nargs='?',default='tabular',choices=['csv','tabular'])
parser.add_argument("-l", "--limit", dest="limit",nargs='?',default=100,type=int)
parser.add_argument("db_name",type=str)
parser.add_argument("table_name",type=str)

template_basic_query='SELECT {} FROM {} WHERE {} LIMIT {}'

#td apikey
apikey=os.getenv("TD_API_KEY")

def printUsageAndExit(msg):
    print msg
    print '\n'
    parser.print_help()
    sys.exit(1)

#validates arguments
def validate(args):
    if args.min_time and args.max_time and args.max_time < args.min_time:
        printUsageAndExit('max time should be greater than min time')

def extract_headers_from_result(schema):
    headers = []
    for column in schema:
        headers.append(column[0])
    return headers

def execute_query(query):
    headers = None
    data = []
    try:
        with tdclient.Client(apikey) as client:
            job = client.query(args.db_name, query)
            # sleep until job's finish
            job.wait()
            print job.result_schema
            headers = extract_headers_from_result(job.result_schema)
            for row in job.result():
                data.append(row)
        return True, headers, data
    except:
        print "Error occured while querying - ", sys.exc_info()[0]
        return False, None, None

def present_output(headers, data):
    if args.format == 'tabular':
        present_as_tabular(headers, data)
    else:
        present_as_csv(headers, data)

# converts a list of random types to a list of strings
def convert_to_str_list(data):
    str_data = []
    for d in data:
        if isinstance(d, str):
            str_data.append(d)
        elif isinstance(d, unicode):
            str_data.append(d.encode('utf-8'))
        else:
            str_data.append(str(d))
    return str_data

def present_as_csv(headers, data):
    header_line = ",".join(headers)
    print header_line
    for row in data:
        str_row = convert_to_str_list(row)
        row_line = ",".join(str_row)
        print row_line

def present_as_tabular(headers, data):
    x = PrettyTable()
    x.field_names = headers
    for row in data:
        x.add_row(row)
    print x

def construct_where_clause(args):
    template_where_clause = ' TD_TIME_RANGE(time, {}, {}) '
    td_min = 'NULL'
    td_max = 'NULL'
    if args.min_time:
        td_min = str(args.min_time)
    if args.max_time:
        td_max = str(args.max_time)

    return template_where_clause.format(td_min, td_max)

def construct_query(args):
    col_list = '*'
    if args.col_list:
        col_list = ','.join(args.col_list)

    limit = args.limit
    from_table = args.table_name
    where_clause = construct_where_clause(args)
    return template_basic_query.format(col_list, from_table, where_clause, limit)

if __name__ == "__main__":
    args = parser.parse_args()
    print args
    validate(args)
    query = construct_query(args)
    success, headers, data  = execute_query(query)
    if success:
        present_output(headers, data)
    sys.exit(0)
