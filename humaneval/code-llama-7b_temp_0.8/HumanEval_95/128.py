
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    # First, get the first key in the dict
    first_key = list(dict.keys())[0]
    # Next, get the case of the first key and set the checker
    if isinstance(first_key, str):
        checker = first_key[0]
        # Check if all the keys are lowercase or all uppercase
        if all(key.lower() == key for key in dict.keys()) or all(key.upper() == key for key in dict.keys()):
            return True
        # If the checker is a lowercase letter and there is a lowercase key, then all keys are lowercase
        elif (checker.islower() or checker.isupper()) and any(key.islower() for key in dict.keys()):
            return False
        # If the checker is a lowercase letter and there is an uppercase key, then all keys are uppercase
        elif (checker.islower() or checker.isupper()) and any(key.isupper() for key in dict.keys()):
            return False
        # If the checker is an uppercase letter and there is a lowercase key, then all keys are uppercase
        elif (checker.islower() or checker.isupper()) and any(key.islower() for key in dict.keys()):
            return False
        # If the checker is an uppercase letter and there is a uppercase key, then all keys are lowercase
        elif (checker.islower() or checker.isupper()) and any(key.isupper() for key in dict.keys()):
            return False
    return False
