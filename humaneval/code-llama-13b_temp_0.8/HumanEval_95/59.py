
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
    key_lower = key_upper = True
    if len(dict) == 0:
        return False
    for k, v in dict.items():
        if not isinstance(k, str):
            return False
        if k.islower():
            key_upper = False
        elif k.isupper():
            key_lower = False
        if not key_lower and not key_upper:
            return False
    return True



