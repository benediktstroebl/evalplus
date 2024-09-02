
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
    return not dict or set(dict.keys()).issubset(set(str(k).lower() for k in dict.keys())) or set(dict.keys()).issubset(set(str(k).upper() for k in dict.keys()))
    
    # if dict == {}:
    #     return True
    # else:
    #     if set(dict.keys()).issubset(set(str(k).lower() for k in dict.keys())):
    #         return True
    #     elif set(dict.keys()).issubset(set(str(k).upper() for k in dict.keys())):
    #         return True
    #     else:
    #         return False
    
    
    # if not dict:
    #     return True
    # if not set(dict.keys()).issubset(set(str(k).lower() for k in dict.keys())) or not set(dict.keys()).issubset(set(str(k).upper() for k in dict.keys())):
    #     return False
    # else:
    #     return True
    
    # if not dict:
    #     return True
    # if not set(dict.keys()).issubset(set(str(k).lower() for k in dict.keys())):
    #     return False
    # else:
    #     return set(dict.keys()).issubset(set(str(k).upper() for k in dict.keys()))
    
    # if not dict:
    #     return True
    # if not set(dict.keys()).issubset(set(str(k).lower() for k in dict.keys())):
    #     return False
    # else:
    #     return set(dict.keys()).issubset(set(str(k).upper() for k in dict.keys()))
    
    # if not dict:
    #     return True
    # if set(dict.keys()).issubset(set(str(k).lower() for k in dict.keys())) or set(dict.keys()).issubset(set(str(k).upper() for k in dict.keys())):
    #     return True
    # else:
