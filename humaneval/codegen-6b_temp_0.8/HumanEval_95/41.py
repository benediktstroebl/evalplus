
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
    if len(dict) == 0:
        return True
    elif len(dict) == 1:
        return check_dict_case(dict[list(dict.keys())[0]])
    else:
        if isinstance(list(dict.keys())[0], str):
            if all(isinstance(value, str) for value in list(dict.values())):
                return True
            elif all(isinstance(value, str) for value in list(dict.values())):
                return check_dict_case(dict)
            elif not all(isinstance(value, str) for value in list(dict.values())):
                return False
        else:
            return False
