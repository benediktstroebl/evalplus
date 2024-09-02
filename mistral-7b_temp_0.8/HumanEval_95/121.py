
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
    all_lower_case_keys = True
    all_upper_case_keys = True
    for key, val in dict.items():
        if key.islower() != True:
            all_lower_case_keys = False
            break
        elif key.isupper() != True:
            all_upper_case_keys = False
            break

    if dict.keys() == 0:
        return False
    if all_lower_case_keys == True or all_upper_case_keys == True:
        return True
    else:
        return False
