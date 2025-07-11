from data import randomuser_data
from randomusers import (
    get_full_names,
    count_users_by_gender,
)

def run_functions() -> None:
    """
    Runs and prints results of all data processing functions for demonstration purposes.
    """
    # print("Full Names:", get_full_names(randomuser_data))
    print(count_users_by_gender(randomuser_data))

run_functions()