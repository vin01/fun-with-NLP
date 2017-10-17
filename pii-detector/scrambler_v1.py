import ner
import csv
import os

tagger = ner.SocketNER(host='localhost', port=8080)

for file in os.listdir("data"):

  print("Processing {0}".format(file))

  with open("data/{0}".format(file)) as csvfile:

        dialect = csv.Sniffer().sniff(csvfile.readline(), [',','\t'])
        csvfile.seek(0)
        content_reader=csv.reader(csvfile, dialect)

        for row in content_reader:
                print(tagger.tag_text(','.join(row))),
