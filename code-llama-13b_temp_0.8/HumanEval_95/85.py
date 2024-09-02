
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
    
    from collections import Counter
    
    if not dict:
        return False
    
    lower_count = Counter(k.islower() for k in dict)
    upper_count = Counter(k.isupper() for k in dict)
    return (lower_count[True] == len(dict)) or (upper_count[True] == len(dict))
    
    
    
    # if not dict:
    #     return False
    # all_keys_lower = []
    # all_keys_upper = []
    # for key in dict:
    #     if key.islower():
    #         all_keys_lower.append(key)
    #     elif key.isupper():
    #         all_keys_upper.append(key)
    #     else:
    #         return False
    # return (all_keys_lower and all_keys_upper) == []
