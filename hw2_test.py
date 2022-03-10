import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"


# Your tests here!
def test_species_count(data):
    assert_equals(3, hw2_pandas.species_count(data))


def test_max_level(data):
    assert_equals(("Lapras", 72), hw2_pandas.max_level(data))


def test_filter_range(data):
    assert_equals(
        ["Arcanine", "Arcanine", "Starmie"], hw2_manual.filter_range(data, 35, 72)
    )


def test_mean_attack_for_type(data):
    assert_equals(47.5, hw2_manual.mean_attack_for_type(data, "fire"))


def test_count_types(data):
    assert_equals({"fire": 2, "water": 2}, hw2_pandas.count_types(data))


def test_mean_attack_per_type(data):
    assert_equals({"fire": 47.5, "water": 140.5}, hw2_manual.mean_attack_per_type(data))


def main():
    spec_test_df = pd.read_csv(SPEC_TEST_FILE)  # a DataFrame
    spec_test_data = parse(SPEC_TEST_FILE)  # a list of dictionaries
    # Feel free to use these datasets in your tests!
    test_species_count(spec_test_df)
    test_max_level(spec_test_df)
    test_filter_range(spec_test_data)
    test_mean_attack_for_type(spec_test_data)
    test_count_types(spec_test_df)
    test_mean_attack_per_type(spec_test_data)


if __name__ == "__main__":
    main()
