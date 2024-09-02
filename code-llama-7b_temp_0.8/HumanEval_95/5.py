
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
    keys = dict.keys()
    all_keys_lowercase = False
    all_keys_uppercase = False
    for key in keys:
        if isinstance(key, str) and key.islower():
            all_keys_lowercase = True
        elif isinstance(key, str) and key.isupper():
            all_keys_uppercase = True
        else:
            return False
    if all_keys_lowercase:
        return True
    elif all_keys_uppercase:
        return True
    elif len(keys) == 0:
        return False
    else:
        return False
