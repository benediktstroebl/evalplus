
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

    keys = list(dict.keys())
    values = list(dict.values())
    if len(keys) == 0 or len(values) == 0:
        return False
    for key in keys:
        if isinstance(key, int):
            return False
        else:
            if key.isupper():
                return False
            else:
                continue
    for value in values:
        if isinstance(value, int):
            return False
        else:
            continue
    return True
    
