
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
    # return False if no keys
    if len(dict) == 0:
        return False
    # return False if more than one case 
    else:
        # determine if more than one case
        is_lower = all(i.islower() for i in dict.keys())
        is_upper = all(i.isupper() for i in dict.keys())
        
        if is_lower or is_upper:
            return True
        else:
            return False
