# Your code here!
import operator
import itertools
from collections import Counter

# fucntion 1
def species_count(data):
    species_name = [a_dict["name"] for a_dict in data]
    # get len of set of a list
    return len(set(species_name))


# function 2
def max_level(data):
    level = [int(a_dict["level"]) for a_dict in data]
    index = level.index(max(level))
    my_name = data[index]["name"]
    my_level = data[index]["level"]
    return my_name, my_level


# Function 3
def filter_range(data, i, j):
    # get all levesls in a list
    level = [int(a_dict["level"]) for a_dict in data]
    # levels that meet condition
    results = [sub for sub in level if (sub < j) & (sub >= i)]
    # indexes of levels that meet the condition
    indexes = []
    for i in results:
        index = level.index(i)
        indexes.append(index)
    # obtain names that meet condition using indexes list
    names = []
    for index in indexes:
        name = data[index]["name"]
        names.append(name)
    return names


# function 4
def mean_attack_for_type(data, group):
    atk_for_certain_type = [
        int(a_dict["atk"]) for a_dict in data if (a_dict["type"] == group)
    ]
    return sum(atk_for_certain_type) / len(atk_for_certain_type)


# Function 5
def count_types(data):
    types = [a_dict["type"] for a_dict in data]
    return Counter(types)


# Function 6
def mean_attack_per_type(data):
    data.sort(key=operator.itemgetter("type"))
    # group the types of pokemon in lists
    list1 = []
    for key, items in itertools.groupby(data, operator.itemgetter("type")):
        list1.append(list(items))
    # create a list of types name and average atk in each type of pokemon
    atk_average_dict = {}
    age_list = []
    for item in list1:
        # the type name
        department = item[0]["type"]
        # the size of pokemon type
        size = len(item)
        sum = 0
        for k in range(size):
            # sum up the atk of each pokemon
            sum += int((item[k]["atk"]))
        average = sum / float(size)
        atk_average_dict
        age_list.append((department, average))
    # return results as a dictionary
    return dict(age_list)
