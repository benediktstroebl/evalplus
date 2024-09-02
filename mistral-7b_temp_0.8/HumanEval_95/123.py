
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
    # Case 1: If the dictionary is empty, return False
    if len(dict) == 0:
        return False
    # Case 2: If all keys are in lower case, return True
    else:
        keys = [key for key in dict.keys()]
        if all(key.islower() for key in keys):
            return True
    # Case 3: If all keys are in upper case, return True
    elif all(key.isupper() for key in keys):
        return True
    # Case 4: If any keys are not in lower or upper case, return False
    else:
        return False
