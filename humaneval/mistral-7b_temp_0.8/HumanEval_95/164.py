
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
        return False
    if len(dict.keys()) == 1:
        return True
    if len(dict.keys()) == 2:
        return dict.keys()[0][0] == dict.keys()[1][0]
    keys = list(dict.keys())
    values = list(dict.values())
    if len(values) != len(set(values)):
        return False
    if len(keys) != len(set(keys)):
        return False
    return True
