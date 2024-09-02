
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
    #pass
    if len(dict) == 0:
        return False
    keynames = dict.keys()
    lowcase_keynames = [key.lower() for key in keynames if type(key) == type("")]
    uppercase_keynames = [key.upper() for key in keynames if type(key) == type("")]
    all_keys = keynames + lowcase_keynames + uppercase_keynames
    all_keys = [key.lower() for key in all_keys]
    if all_keys == keynames:
        return True
    else:
        return False