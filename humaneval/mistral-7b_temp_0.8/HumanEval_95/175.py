
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
    # if type(dict) != dict:
    #     raise TypeError("The argument should be a dictionary")
    if len(dict) == 0:
        return False
    keys = list(dict.keys())
    if len(set([type(x) for x in keys])) > 1:
        raise TypeError("The dictionary should only have string keys")
    value_set = set()
    for key in keys:
        if type(key) == str:
            if key.isupper() and key in value_set:
                return False
            if key.islower() and key not in value_set:
                return False
            if key not in value_set:
                value_set.add(key.upper())
    return True
