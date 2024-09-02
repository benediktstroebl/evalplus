
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

    dict_keys = list(dict.keys())
    if len(dict_keys) == 0:
        return False
    elif len(dict_keys) == 1:
        if type(dict_keys[0]) == str:
            return True
        else:
            return False
    else:
        key_len = len(dict_keys)
        i = 0
        while i < key_len:
            if type(dict_keys[i])!= str:
                return False
            i += 1
        return True
