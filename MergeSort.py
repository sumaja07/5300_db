import os
import pandas as pd
import csv
from datetime import date, datetime
initTime = 0
finalTime = 0

def mergeSort():
    print(datetime.now())
    Data = "./data/"
    toMerge = os.listdir(Data)
    files_left = len(toMerge)
    count = 1
    while count < files_left:
        file = Data + "dataset_{0}.csv".format(count)
        df = pd.read_csv(file)
        sort_df = df.sort_values(by=["title"])
        sort_df.to_csv("./sorted_data/dataset_{0}_sorted.csv".format(count))
        count += 1


def linear_search():
    Data = "./sorted_data/"
    toMerge = os.listdir(Data)
    files_left = len(toMerge)
    count = 1
    notFound = True
    while count < files_left and notFound == True:
        file = Data + "dataset_{0}_sorted.csv".format(count)
        csv_file = csv.reader(open(file, "r", encoding='utf8'), delimiter=",")
        rowCount = 0
        for row in csv_file:
            rowCount += 1
            if "Sandman: Dream Hunters 30th Anniversary Edition" == row[26]:
                print('\n' + "Located in: " + str(file))
                print("Row: " + str(rowCount))
                print(str(row)  +'\n')
                notFound = False
                print(datetime.now())
        count += 1



mergeSort()
linear_search()
