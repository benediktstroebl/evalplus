import unittest
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dict:
        return False
    lowercase_count, uppercase_count = 0, 0
    for key in dict.keys():
        if isinstance(key, str):
            if key.islower():
                lowercase_count += 1
            elif key.isupper():
                uppercase_count += 1
        else:
            return False
    return (lowercase_count == len(dict) or uppercase_count == len(dict))