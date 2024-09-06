
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
    if not dict:
        return False
    
    keys = list(dict.keys())
    values = list(dict.values())
    key1, key2 = keys[0], keys[1]
    value1, value2 = values[0], values[1]
    if not isinstance(key1, str) or not isinstance(key2, str):
        return False
    elif key1.islower() and key2.islower():
        return check_dict_case(dict)
    elif key1.isupper() and key2.isupper():
        return check_dict_case(dict)
    return False
