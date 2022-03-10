# Your code here!
# function 1
def species_count(data):
    count = data["name"]
    count = count.nunique()
    return count


# function 2
def max_level(data):
    max_index = data["level"].idxmax()
    max_values = data.iloc[max_index][["name", "level"]]
    return tuple(max_values)


# function 3
def filter_range(data, i, j):
    filtered_level = data[data["level"].isin(range(i, j))]["name"]
    return list(filtered_level)


# function 4
def mean_attack_for_type(data, group):
    group_df = data[data["type"] == group]
    atk_mean = group_df["atk"].mean()
    return atk_mean


# fucntion 5
def count_types(data):
    type_count = data["type"].value_counts()
    return type_count.to_dict()


# function 6
def mean_attack_per_type(data):
    each_type_attack_mean = data.groupby("type")["atk"].mean()
    return each_type_attack_mean.to_dict()
