from data import randomuser_data
from randomusers import (
    get_full_names,
    get_users_by_country,
    count_users_by_gender,
    get_emails_of_older_than,
    get_usernames_starting_with,
    get_average_age,
    group_users_by_nationality,
    get_all_coordinates,
    get_oldest_user,
    find_users_in_timezone,
    get_registered_before_year
)

def run_functions() -> None:
    """
    Runs and prints results of all data processing functions for demonstration purposes.
    """
    # print("Full Names:", get_full_names(randomuser_data))
    # print(get_users_by_country(randomuser_data,'India'))
    # print(count_users_by_gender(randomuser_data))
    # print(get_emails_of_older_than(randomuser_data,60))
    # print(get_usernames_starting_with(randomuser_data,'g') )
    # print(get_average_age(randomuser_data))
    # print(group_users_by_nationality(randomuser_data))
    # print(get_all_coordinates(randomuser_data))
    # print(get_oldest_user(randomuser_data))
    # print(find_users_in_timezone(randomuser_data,'+3:30'))
    print(get_registered_before_year(randomuser_data,2011))



run_functions()