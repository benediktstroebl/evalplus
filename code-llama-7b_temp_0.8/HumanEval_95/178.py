
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
    
    # assert type(dict) == dict, "Input must be a dictionary"
    
    is_all_upper = None
    is_all_lower = None
    
    if len(dict.keys()) > 0:
        
        is_all_upper = all(isinstance(k, str) and k.isupper() for k in dict.keys())
        is_all_lower = all(isinstance(k, str) and k.islower() for k in dict.keys())
        
        return is_all_lower if is_all_upper else is_all_upper
    
    else:
        return False
