
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
    if dict == {}:
        return False
    dict_lower = {}
    dict_upper = {}
    for key in dict:
        if key.isupper():
            dict_upper[key] = dict[key]
        elif key.islower():
            dict_lower[key] = dict[key]
        else:
            return False
    if len(dict_lower) == 0:
        return True
    if len(dict_upper) == 0:
        return True
    if len(dict_lower) == len(dict_upper):
        return True
    return False
    # return
