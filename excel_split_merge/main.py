import os
import pandas as pd
from os.path import isfile, join


def quantity(xls):
    count = 0
    for xls in xls.sheet_names:
        count += 1
    return count


def tabs2sheet(filename):
    xls = pd.ExcelFile(filename + '.xlsx')
    path = 'data'

    if not os.path.exists(path):
        os.makedirs(path)

    for x in range(quantity(xls)):
        file = xls.parse(x)
        filename = xls.sheet_names[x] + '.xlsx'
        file.to_excel('data/'+filename, index=False)


def sheets2tabs(folder):
    files = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    writer = pd.ExcelWriter('new_data.xlsx', engine='xlsxwriter')

    for title in files:
        df = pd.read_excel('data/' + title)
        df.to_excel(writer, sheet_name=title[0:31])

    writer.save()


def start():
    val = input("Enter 1 for split, 2 for merge: ")
    if val == '1':
        filename = input('Enter the file name without the extension: ')
        tabs2sheet(filename)
    else:
        folder = input('Please enter the directory name: ')
        sheets2tabs(folder)


if __name__ == '__main__':
    start()
