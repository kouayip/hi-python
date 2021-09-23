import json
import csv
import sys

def json_to_csv(file_path, csv_file_name):
    with open(file_path) as json_file:
        data = json.l
        headers = data[0].keys()

        with open(csv_file_name, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)

            for record in data:
                r = (value for value in record.values())
                writer.writerow(r)

if __name__ == "__main__":
    if len(sys.argv) >= 1:
        file_path = sys.argv[1]
        csv_file_name = "output.csv"

        if file_path.lower().endswith('.json'):
            print ("program start...")
            json_to_csv(file_path, csv_file_name)
            print ("final process, the conversion was completed")
        else: 
            print ("*error* file type error")
    else: 
        print ("*error* the program needs a file as an argument")