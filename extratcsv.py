import csv
import sys
if len(sys.argv) != 2:
    print("rong input ")
    exit()
lon = sys.argv[1]
with open(lon, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    i=0
    for row in csvreader:
        print(row)
        print(i)
        i=i+1
