
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
    is_all_lower = True
    is_all_upper = True
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if is_all_lower and not key.islower():
            is_all_lower = False
        if is_all_upper and not key.isupper():
            is_all_upper = False
    return is_all_lower or is_all_upper
    
