
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
    # obtain the set of keys in the dict
    set_keys = set(dict.keys())
    # check if there are any duplicate keys in the set
    if len(set_keys) != len(dict.keys()):
        return False
    # check if all keys are lower case
    for key in set_keys:
        if key != key.lower():
            return False
    # check if all keys are upper case
    for key in set_keys:
        if key != key.upper():
            return False
    # if we have come here, all keys are either lower or upper case.
    return True


