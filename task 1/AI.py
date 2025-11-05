# Copilot suggestion for sorting list of dictionaries
def sort_dicts(data, key, reverse=False):
    """Sort list of dictionaries by given key."""
    try:
        return sorted(data, key=lambda item: item.get(key, 0), reverse=reverse)
    except TypeError as e:
        print(f"Error while sorting: {e}")
        return data

# Example usage
people = [
    {"name": "Ellen", "age": 25},
    {"name": "Grace", "age": 30},
    {"name": "Paul", "age": 22}
]

print(sort_dicts(people, "age"))
