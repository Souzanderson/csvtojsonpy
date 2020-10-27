from libs.csvtojson import CsvToJson

if __name__ == "__main__":
    csvtojson = CsvToJson("todos.csv")
    dc = csvtojson.toDic()
    print(dc)
    csvtojson.toJson()