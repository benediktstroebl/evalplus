
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

    keys = list(dict.keys())
    # Checking if all keys are in lower case.
    lower_keys = []
    for i in keys:
        if i.islower():
            lower_keys.append(i)
    # Checking if all keys are in upper case.
    upper_keys = []
    for i in keys:
        if i.isupper():
            upper_keys.append(i)

    if len(lower_keys) == len(keys):
        return True
    elif len(upper_keys) == len(keys):
        return True
    else:
        return False

