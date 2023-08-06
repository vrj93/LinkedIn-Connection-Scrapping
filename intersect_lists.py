import json

def print_values_not_in_file(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1:
        json_data1 = json.load(f1)

    with open(file2, "r", encoding="utf-8") as f2:
        json_data2 = json.load(f2)

    value_set1 = set(json_data1)
    value_set2 = set(json_data2)

    values_not_in_file2 = value_set1 - value_set2

    for value in values_not_in_file2:
        print(value)

if __name__ == "__main__":
    file1 = "connections.json"
    file2 = "followers.json"
    print_values_not_in_file(file1, file2)
