import os
import pandas as pd
import csv
from datetime import date, datetime
import json
initTime = 0
finalTime = 0

def hash_index():
    print(datetime.now())

    Data = "./data/"
    toMerge = os.listdir(Data)
    remFiles = len(toMerge)
    count = 1
    notFound = True
    while count < remFiles and notFound:
        file = Data + "dataset_{0}.csv".format(count)
        
        reader = csv.reader(open(file, encoding='utf8'))
        result = {}
        for row in reader:
            key = row[25]
            if(key in result):
                pass
            result[key] = row[0:24]
        
        if "Sandman: Dream Hunters 30th Anniversary Edition" in result:
            print('\n' + "Located in: " + str(file))
            print(str(result["Sandman: Dream Hunters 30th Anniversary Edition"])  +'\n')
            notFound = False
            print(datetime.now())

        count += 1

hash_index()
