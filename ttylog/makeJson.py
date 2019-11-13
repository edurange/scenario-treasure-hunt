import csv
import json
import sys

csvFile = open(sys.argv[1], 'r')
jsonFile = open(sys.argv[2], 'w')

fields = ["begin", "host", "time", "cwd", "cmd", "output", "prompt"]
arr = []
reader = csv.reader(csvFile, delimiter=',', quotechar='%', quoting=csv.QUOTE_MINIMAL)

for row in reader:
    lineStr = ''
    for i,item in enumerate(row):
        if i == 0:
            lineStr += '{'
        if i == 5:
            item = item.replace("\r", "").replace("\n", "")
        lineStr += '"'+fields[i]+'":"' + item.strip('\n\r').replace('\"', '') + '"'
        if i != 6:
            lineStr += ','
        else:
            lineStr += '}\n'
    arr.append(lineStr)
for a in arr:
    jsonFile.write(a)



