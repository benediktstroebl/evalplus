
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
    # version 1
    if dict == {}:
        return False
    dict_keys_lower = [key for key in dict.keys() if key.islower()]
    dict_keys_upper = [key for key in dict.keys() if key.isupper()]
    if dict_keys_lower == [] and dict_keys_upper == []:
        return False
    if len(dict_keys_lower) > 0 and len(dict_keys_upper) == 0:
        return True
    if len(dict_keys_lower) == 0 and len(dict_keys_upper) > 0:
        return True
    return False
    
    # version 2
    # if dict == {}:
    #     return False
    # dict_keys_lower = [key for key in dict.keys() if key.islower()]
    # dict_keys_upper = [key for key in dict.keys() if key.isupper()]
    # if (dict_keys_lower == [] and dict_keys_upper != []) or (dict_keys_upper == [] and dict_keys_lower != []):
    #     return False
    # return True
    
    # version 3
    # if len(dict) == 0:
    #     return False
    # upper_count = 0
    # lower_count = 0
    # for i in dict.keys():
    #     if i.islower():
    #         lower_count += 1
    #     if i.isupper():
    #         upper_count += 1
    # if lower_count == 0 and upper_count == 0:
    #     return False
    # if lower_count == 0 and upper_count != 0:
    #     return False
    # if upper_count == 0 and lower_count != 0:
    #     return False
    # return True

    # version 4
    # if dict == {}:
    #     return False
    # for key in dict.keys():
    #     if not key.islower() and not key.isupper():
    #         return False
    # return True

    # version 
