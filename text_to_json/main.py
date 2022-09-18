import json
import pandas as pd

file = input("Please enter the filename: ")
mode = input("\nPlease select mode:\n1. To CSV\n2. To JSON\n")


def read_file(filename):
    data = []
    mapping = {}
    with open(filename + '.txt') as f:
        content = f.readlines()

        for i in range(len(content)):
            value = content[i].split(',')
            if i == 0:
                for x in value:
                    d = x.replace('\n', "")
                    d = d.replace('"', "")
                    d = d.replace('\u0303', "")
                    d = d.replace('\u00b4', "")
                    d = d.replace('\\', "")
                    mapping[d] = ""
                    data.append(d)

            else:
                for x in range(len(data)):
                    z = value[x].replace("\n", "")
                    z = z.replace('"', "")
                    z = z.replace('\u0303', "")
                    z = z.replace('\u00b4', "")
                    z = z.replace('\\', "")
                    mapping[data[x]] += z + ', '

        for i in data:
            mapping[i] = mapping[i][:-2]
        return mapping


dict = read_file(file)


def to_csv(dict):
    with open(file + '.csv', 'w') as f:
        keys = list(dict.keys())
        df = pd.DataFrame()
        for i in range(len(keys)):
            df[keys[i]] = dict[keys[i]].split(', ')
        df.to_csv(file + '.csv', index=False, header=True)
        print("Done Converting: " + file + '.csv')


def to_json(dict):
    with open(file + '.json', "w") as f:
        json.dump(dict, f)
        print("Done Converting: " + file + '.json')


if int(mode) == 1:
    to_csv(dict)
elif int(mode) == 2:
    to_json(dict)
else:
    print("Error reading convert mode..")



