import os
import csv
import textwrap
import logging
from datetime import date

searched_domain = ""
reference_id = ""
dict_input_csv_all = {}
a = 0


class Genom:
    def __init__(self, id, genome, count, mutation, isDomainPresent):
        self.id = id
        self.genome = genome
        self.count = count
        self.mutation = mutation
        self.isDomainPresent = isDomainPresent


with open('genomes.csv', newline='') as input_csv:
    all = csv.reader(input_csv)
    for row in all:
        if row[0] == "id" and row[1] == "genome":
            print("ok")
        if row[0] == "M_AURIS_702100":
            reference_id = row[1]
            #print(reference_id)
        if row[1] != reference_id:
            a += 1
            print(a)
        dict_input_csv_all[row[0]] = Genom(row[0], row[0], row[0], row[0], row[0])

    # for i in sorted(dict_input_csv_all):
    #     print(i)

with open('final.csv', 'w') as out_csv:
    fieldnames = ["id", "genome", "count", "mutation", "isDomainPresent"]
    csv_write = csv.DictWriter(out_csv, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
    csv_write.writeheader()

    for value in dict_input_csv_all.values():
        csv_write.writerow({
            "id": value.id,
            "genome": value.genome,
            "count": value.count,
            "mutation": value.mutation,
            "isDomainPresent": value.isDomainPresent
        })

    # for key, value in dict_input_csv_all.items():
    #     Test_row = "key: %s | value: %s | %s | %s | %s" % (key, value.genome, value.id, value.id, value.id)
    #     logging.basicConfig(filename=str(date) + " logs.log", filemode='w', level=logging.INFO)
    #     logging.info(Test_row)
