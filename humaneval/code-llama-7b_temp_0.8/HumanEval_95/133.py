
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
    is_lower_case = False
    is_upper_case = False
    if len(dict) == 0:
        return False
    elif len(dict) == 1:
        return True
    for key, value in dict.items():
        if isinstance(key, str):
            if key.islower():
                is_lower_case = True
            elif key.isupper():
                is_upper_case = True
            else:
                return False
    if is_lower_case == is_upper_case:
        return False
    else:
        return True

