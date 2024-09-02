
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
    
    #Solution 1
    # if len(dict) == 0:
    #     return False
    # for key in dict:
    #     if not type(key) == str:
    #         return False
    #     elif not isinstance(key, str):
    #         return False
    #     elif not key.islower():
    #         return False
    # return True

    #Solution 2
    return len(dict) > 0 and all([type(key) == str for key in dict]) and\
        all([key.isupper() or key.islower() for key in dict])

