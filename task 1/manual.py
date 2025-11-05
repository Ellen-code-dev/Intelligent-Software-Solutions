# Manual implementation of sorting a list of dictionaries by a given key
def sort_list_of_dicts(data_list, sort_key):
    """
    Sorts a list of dictionaries in ascending order by the specified key.
    Args:
        data_list (list): List of dictionaries to sort
        sort_key (str): Key to sort the dictionaries by
    Returns:
        list: A new sorted list of dictionaries
    """
    return sorted(data_list, key=lambda x: x[sort_key])

# Example usage
employees = [
    {"name": "Ellen", "age": 25, "salary": 50000},
    {"name": "Grace", "age": 30, "salary": 60000},
    {"name": "Paul", "age": 22, "salary": 45000}
]

sorted_employees = sort_list_of_dicts(employees, "age")
print(sorted_employees)
