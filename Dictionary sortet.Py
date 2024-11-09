
def sort_dictionary_by_keys(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict
user_input = input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): ")

try:
    user_dict = eval(user_input)
    if isinstance(user_dict, dict):
        sorted_dict = sort_dictionary_by_keys(user_dict)
        print("Sorted dictionary:", sorted_dict)
    else:
        print("Please enter a valid dictionary.")
except:
    print("Invalid input. Please enter a dictionary in the correct format.")
