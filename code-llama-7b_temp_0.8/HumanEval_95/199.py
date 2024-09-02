
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
    keys = dict.keys()
    lower_case = []
    upper_case = []
    if len(keys) == 0:
        return False
    for key in keys:
        if isinstance(key, str):
            if key.islower():
                lower_case.append(key)
            elif key.isupper():
                upper_case.append(key)
            else:
                return False
        else:
            return False
    if lower_case == keys or upper_case == keys:
        return True
    else:
        return False
    
    # Check if all keys are lower case.
    # lower_case = [key for key in keys if key.islower()]
    # if all(lower_case) == keys:
    #     return True

    # Check if all keys are upper case.
    # upper_case = [key for key in keys if key.isupper()]
    # if all(upper_case) == keys:
    #     return True
    # else:
    #     return False

    # return all([key.islower() for key in keys]) or all([key.isupper() for key in keys])




