import csv
import json

class CsvToJson:
    def __init__(self, location):
      self._location = location
      self._arr = {}

    def toJson(self, savelocation="req"):
        with open('%s.json' % (savelocation), 'w') as fp:
            json.dump(self._arr, fp, sort_keys=True, indent=4)
    
    def toDic(self):
        with open(self._location, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            header = reader.__next__()
            for row in reader:
                if(row):
                    self._arr[row[4]] = {}
                    for i in range(len(row)):
                        self._arr[row[4]][header[i]] = row[i]
        return self._arr