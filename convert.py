import csv
import json

csvfile = open('addresses.csv', 'r')
jsonfile = open('addresses.json', 'w')

fieldnames = ("FirstName","LastName","Street","City","State","Zipcode")
reader = csv.DictReader( csvfile, fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')