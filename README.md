\# Treasuredata_excercise
This simple program lets you upload data and then query based on treasuredata

# Requirements
The code is written in the following Python Version
Python 2.7+


## Install

You can install the releases from PyPI.

$ pip install certifi

$ pip install PTable

## Data

Data is uploaded at the following location
Database name : Interview
Table name    : movies

## Running Tests

#### 1. Execution Works properly and movie data is extracted 
##### Command : 'TD_API_KEY=‘9506/021bd0a0e1d94c2d3aa3e8aeba5d7156b8415f04’ python prog.py interview movies -e hive -f csv --min 300000  -c original_title popularity'

db_name = interview
table_name = movies
Engine = hive
Min = minimum timestamp
Max = max timestamp
C = column list
Result : File displayed in tabular form 
#### 2. Engine defaulted to presto when engine option not specified
 
##### Command : 'TD_API_KEY=‘9506/021bd0a0e1d94c2d3aa3e8aeba5d7156b8415f04' python prog.py interview movies —f csv --min 300000  -c original_title popularity'

##### Parameters taken

Namespace(col_list=['original_title', 'popularity'], db_name='interview', engine='presto', format='csv', limit=100, max_time=None, min_time=300000L, table_name='movies')

##### Result : File displayed in csv format
Hive 193356808

#### 3. Error when given base as the option for engine

##### Command : 'TD_API_KEY=‘9506/021bd0a0e1d94c2d3aa3e8aeba5d7156b8415f04' python prog.py interview movies -e hbase —f csv --min 300000  -c original_title popularity'

##### Error:
usage: prog.py [-h] [-c COL_LIST [COL_LIST ...]] [-m MIN_TIME] [-M MAX_TIME]
               [-e [{hive,presto}]] [-f [{csv,tabular}]] [-l [LIMIT]]
               db_name table_name
prog.py: error: argument -e/--engine: invalid choice: 'hbase' (choose from 'hive', ‘presto')

#### 4. Error thrown when Format specified as xml

##### Command : 'TD_API_KEY=‘9506/021bd0a0e1d94c2d3aa3e8aeba5d7156b8415f04' python prog.py interview movies -e hive -f xml --min 300000  -c original_title popularity'

##### Error:
usage: prog.py [-h] [-c COL_LIST [COL_LIST ...]] [-m MIN_TIME] [-M MAX_TIME]
               [-e [{hive,presto}]] [-f [{csv,tabular}]] [-l [LIMIT]]
               db_name table_name
prog.py: error: argument -f/--format: invalid choice: 'xml' (choose from 'csv', ‘tabular')
#### 5. Error thrown when min timestamp greater than max timestamp
##### Command: 'TD_API_KEY=‘9506/021bd0a0e1d94c2d3aa3e8aeba5d7156b8415f04' python prog.py interview movies -e hive -f csv --min 300000 --max 1  -c original_title popularity'

##### Error :
 Namespace(col_list=['original_title', 'popularity'], db_name='interview', engine='hive', format='csv', limit=100, max_time=1L, min_time=300000L, table_name='movies')
max time should be greater than min time


usage: prog.py [-h] [-c COL_LIST [COL_LIST ...]] [-m MIN_TIME] [-M MAX_TIME]
               [-e [{hive,presto}]] [-f [{csv,tabular}]] [-l [LIMIT]]
               db_name table_name

positional arguments:
  db_name
  table_name

optional arguments:
  -h, --help            show this help message and exit
  -c COL_LIST [COL_LIST ...], --column COL_LIST [COL_LIST ...]
  -m MIN_TIME, --min MIN_TIME
  -M MAX_TIME, --max MAX_TIME
  -e [{hive,presto}], --engine [{hive,presto}]
  -f [{csv,tabular}], --format [{csv,tabular}]
  -l [LIMIT], --limit [LIMIT]

#### 6. Data generated in tabular format

##### Command : 'TD_API_KEY='9506/021bd0a0e1d94c2d3aa3e8aeba5d7156b8415f04' python prog.py interview movies -e hive -c original_title popularity'

##### Result: Hive 194164066

\+----------------------------------------------------------------+------------+\
\|                         original_title                         | popularity |\
\+----------------------------------------------------------------+------------+\
\|                             Avatar                             \| 150.437577 |\
\|            Pirates of the Caribbean: At World's End            \| 139.082615 |\
\|                            Spectre                             | 107.376788 |\
\|                     The Dark Knight Rises                      | 112.31295  |\
\|                          John Carter                           | 43.926995  |\
\|                          Spider-Man 3                          | 115.699814 |\
\|                            Tangled                             | 48.681969  |\
\|                    Avengers: Age of Ultron                     | 134.279229 |\
\|             Harry Potter and the Half-Blood Prince             | 98.885637  |\
\|               Batman v Superman: Dawn of Justice               | 155.790452 |\
\|                        Superman Returns                        | 57.925623  |\
\|                       Quantum of Solace                        | 107.928811 |\
\|           Pirates of the Caribbean: Dead Man's Chest           | 145.847379 |\
\|                        The Lone Ranger                         | 49.046956  |\
\|                          Man of Steel                          | 99.398009  |\
\|            The Chronicles of Narnia: Prince Caspian            | 53.978602  |\
\|                          The Avengers                          | 144.448633 |\
\|          Pirates of the Caribbean: On Stranger Tides           | 135.413856 |\
\|                         Men in Black 3                         | 52.035179  |\
\|           The Hobbit: The Battle of the Five Armies            | 120.965743 |\
\|                     The Amazing Spider-Man                     | 89.866276  |\
\|                           Robin Hood                           | 37.668301  |\
\|              The Hobbit: The Desolation of Smaug               | 94.370564  |\
\|                       The Golden Compass                       | 42.990906  |\
\|                           King Kong                            |  61.22601  |\
\|                            Titanic                             | 100.025899 |\
\|                   Captain America: Civil War                   | 198.372395 |\
\|                           Battleship                           | 64.928382  |\
\|                         Jurassic World                         | 418.708552 |\
\|                            Skyfall                             | 93.004993  |\
\|                          Spider-Man 2                          | 35.149586  |\
\|                           Iron Man 3                           |  77.68208  |\
\|                      Alice in Wonderland                       | 78.530105  |\
\|                     X-Men: The Last Stand                      |  3.857526  |\
\|                      Monsters University                       | 89.186492  |\
\|              Transformers: Revenge of the Fallen               | 21.939663  |\
\|                Transformers: Age of Extinction                 | 116.840296 |\
\|                   Oz: The Great and Powerful                   | 46.985445  |\
\|                    The Amazing Spider-Man 2                    | 89.270217  |\
\|                          TRON: Legacy                          |  73.79505  |\
\|                             Cars 2                             |  49.98659  |\
\|                         Green Lantern                          | 51.872839  |\
\|                          Toy Story 3                           | 59.995418  |\
\|                      Terminator Salvation                      | 71.862892  |\
\|                           Furious 7                            | 102.322217 |\
\|                          World War Z                           | 81.834855  |\
\|                   X-Men: Days of Future Past                   | 118.078691 |\
\|                    Star Trek Into Darkness                     | 78.291018  |\
\|                     Jack the Giant Slayer                      | 43.349855  |\
\|                        The Great Gatsby                        | 61.196071  |\
\|              Prince of Persia: The Sands of Time               | 62.169881  |\
\|                          Pacific Rim                           | 56.523205  |\
\|                 Transformers: Dark of the Moon                 | 28.529607  |\
\|       Indiana Jones and the Kingdom of the Crystal Skull       | 75.674458  |\
\|                       The Good Dinosaur                        | 51.692953  |\
\|                             Brave                              | 125.114374 |\
\|                        Star Trek Beyond                        | 65.352913  |\
\|                             WALL·E                             | 66.390712  |\
\|                          Rush Hour 3                           |  22.57178  |\
\|                              2012                              | 45.274225  |\
\|                       A Christmas Carol                        | 39.744242  |\
\|                       Jupiter Ascending                        |  85.36908  |\
\|                      The Legend of Tarzan                      | 42.741719  |\
\| The Chronicles of Narnia: The Lion, the Witch and the Wardrobe | 67.391328  |\
\|                       X-Men: Apocalypse                        | 139.272042 |\
\|                        The Dark Knight                         | 187.322927 |\
\|                               Up                               | 92.201962  |\
\|                       Monsters vs Aliens                       | 36.167578  |\
\|                            Iron Man                            | 120.725053 |\
\|                              Hugo                              | 32.319043  |\
\|                         Wild Wild West                         | 40.748915  |\
\|             The Mummy: Tomb of the Dragon Emperor              | 60.034162  |\
\|                         Suicide Squad                          |  90.23792  |\
\|                         Evan Almighty                          | 27.082182  |\
\|                        Edge of Tomorrow                        | 79.456485  |\
\|                           Waterworld                           | 44.640292  |\
\|                  G.I. Joe: The Rise of Cobra                   | 32.852443  |\
\|                           Inside Out                           | 128.655964 |\
\|                        The Jungle Book                         | 94.199316  |\
\|                           Iron Man 2                           | 77.300194  |\
\|                  Snow White and the Huntsman                   | 77.178973  |\
\|                           Maleficent                           | 110.620647 |\
\|                 Dawn of the Planet of the Apes                 | 243.791743 |\
\|                           The Lovers                           |  2.418535  |\
\|                            47 Ronin                            | 41.796339  |\
\|              Captain America: The Winter Soldier               | 72.225265  |\
\|                      Shrek Forever After                       | 44.041186  |\
\|                          Tomorrowland                          | 130.311355 |\
\|                           Big Hero 6                           | 203.73459  |\
\|                         Wreck-It Ralph                         | 62.341073  |\
\|                       The Polar Express                        | 47.323228  |\
\|                  Independence Day: Resurgence                  | 48.775723  |\
\|                    How to Train Your Dragon                    | 67.263269  |\
\|               Terminator 3: Rise of the Machines               | 69.405188  |\
\|                    Guardians of the Galaxy                     | 481.098624 |\
\|                          Interstellar                          | 724.247784 |\
\|                           Inception                            | 167.58371  |\
\|                          シン・ゴジラ                          |  9.476999  |\
\|               The Hobbit: An Unexpected Journey                | 108.849621 |\
\|                    The Fast and the Furious                    |  6.909942  |\
\+----------------------------------------------------------------+------------+
