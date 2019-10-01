import csv
import glob
import sqlite3
import sys
from os import path


INPUT_PATH = '../09_30_2019_DataDump/ParsedMonos'
OUTPUT_PATH = '../output/data.db'


if path.exists(OUTPUT_PATH):
  print('dB already exists. Will not overwrite.')
  sys.exit()

con = sqlite3.connect(OUTPUT_PATH)
cur = con.cursor()

for f in glob.glob(f'{INPUT_PATH}/*.txt'):
  with open(f, encoding='utf-8', newline='') as file:
    table_name = path.splitext(path.basename(f))[0]
    if table_name == 'TextLabel':
      continue

    reader = csv.reader(file)
    columns = next(reader)
    rows = [tuple(row) for row in reader]
    placeholder = ','.join(["?" for i in columns])
    print(f'============{table_name}============')

    cur.execute(f'CREATE TABLE {table_name} ({",".join(columns)})')
    cur.executemany(f'INSERT INTO {table_name} VALUES ({placeholder})', rows)

con.commit()
con.close()