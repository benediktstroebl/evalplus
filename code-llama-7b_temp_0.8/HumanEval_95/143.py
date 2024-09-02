
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
    is_upper = False
    is_lower = False
    for key in dict:
        if isinstance(key, str):
            if key.islower():
                is_lower = True
            if key.isupper():
                is_upper = True
        else:
            return False
    return is_lower or is_upper
    
    
    # one-liner
    # return not any([not isinstance(key, str) for key in dict]) and (all([key.islower() for key in dict]) or all([key.isupper() for key in dict]))

