
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
    # For each key in the dictionary, check if the key is in lower or upper case.
    # If the key is in lower case, set LOWER to True, and set UPPER to False.
    # If the key is in upper case, set UPPER to True, and set LOWER to False.
    # If the key is not in lower or upper case, set BOTH to False.
    # If any key is not in the same case as the previous key, return False.
    # If all keys are in the same case, return True.
    # If the dictionary is empty, return False.
    if dict == {}:
        return False
    else:
        LOWER = True
        UPPER = True
        BOTH = True
        for key in dict.keys():
            if key.islower():
                if UPPER:
                    return False
                UPPER = False
            elif key.isupper():
                if LOWER:
                    return False
                LOWER = False
            else:
                if not (LOWER or UPPER):
                    return False
        return BOTH
