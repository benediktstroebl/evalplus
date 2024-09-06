
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
    keys_lower = []
    keys_upper = []
    keys_empty = []
    keys_mix = []

    # Check for empty keys.
    for key in keys:
        if key == '':
            keys_empty.append(key)

    # If there are empty keys, return False.
    if len(keys_empty) > 0:
        return False

    # Check for keys that are all lower case.
    for key in keys:
        if str(key).islower():
            keys_lower.append(key)

    # If all keys are lower case, return True.
    if len(keys_lower) == len(keys):
        return True

    # Check for keys that are all upper case.
    for key in keys:
        if str(key).isupper():
            keys_upper.append(key)

    # If all keys are upper case, return True.
    if len(keys_upper) == len(keys):
        return True

    # Check for keys that are a mix of upper and lower case.
    for key in keys:
        if str(key).islower() is False and str(key).isupper() is False:
            keys_mix.append(key)

    # If there are any keys that are a mix of upper and lower case, return False.
    if len(keys_mix) > 0:
        return False

    # Otherwise return True.
    return True














