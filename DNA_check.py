import os
import click
import csv
import logging
from datetime import date


@click.command()
# @click.option('--h', help='Simple program to identifying common mutations and analyzing genomes for the existence of specific substrings')
@click.option('--input_csv', prompt='Path to input CSV', help='Path to input CSV')
@click.option('--out_vis', prompt='Path to output pdf', help='Path to output pdf')
@click.option('--out_csv', prompt='Path to output CSV', help='Path to output CSV')
@click.option('--searched_domain', prompt='String to be searched', help='String to be searched')
@click.option('--reference_id', prompt='ID of the reference genome', help='ID of the reference genome')
def datas_check(input_csv, out_vis, out_csv, searched_domain, reference_id):
    """Simple program to identifying
    common mutations and analyzing genomes for the existence of specific
    substrings."""
    if input_csv:
        pass
    else:
        raise Exception("Lack of file name")

    if out_vis:
        pass
    else:
        raise Exception("Lack of file name")

    if out_csv:
        pass
    else:
        raise Exception("Lack of file name")

    if searched_domain:
        pass
    else:
        raise Exception("Lack of searched domain")

    if reference_id:
        pass
    else:
        raise Exception("Lack of reference id")


searched_domain = ""
reference_id = ""
dict_input_csv_all = {}
a = 0
date = date.today()


class Genom:
    def __init__(self, id, genome, count, mutation, isDomainPresent):
        self.id = id
        self.genome = genome
        self.count = count
        self.mutation = mutation
        self.isDomainPresent = isDomainPresent


#def open_input(input_csv):
    print(input_csv)
    # with open(input_csv, newline='') as input_csv:
    #     all = csv.reader(input_csv)
    #     print("Type searched part of DNA: ")
    #     searched_domain = input()
    #     for row in all:
    #         if row[0] == "id" and row[1] == "genome":
    #             print("ok")
    #     if row[0] == "M_AURIS_702100":
    #         reference_id = row[1]
    #         # print(reference_id)
    #     if row[1] != reference_id:
    #         # print(a)
    #         pass
    #     dict_input_csv_all[row[0]] = Genom(row[0], row[0], row[0], row[0], row[0])
    #
    #     if searched_domain in row[1]:
    #         # a += 1
    #         # print(a)
    #         pass
    #
    #     if not "A" and "C" and "T" and "G" and "N" in row[1]:
    #         a += 1
    #         print(a)
    #
    # # for i in sorted(dict_input_csv_all):
    # #     print(i)


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

    #
    # for key, value in dict_input_csv_all.items():
    #     genome_row = "key: %s | value: %s | %s | %s | %s" % (key, value.id, value.genome, value.count, value.mutation, value.isDomainPresent)
    #     logging.basicConfig(filename=str(date) + " logs.log", filemode='w', level=logging.INFO)
    #     logging.info(genome_row)

if __name__ == '__main__':
    datas_check()
