
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

    # Solution 1:
    # if len(dict) == 0:
    #     return False
    # upper_count = 0
    # lower_count = 0
    # for k in dict:
    #     if type(k) is str:
    #         if k.isupper():
    #             upper_count += 1
    #         elif k.islower():
    #             lower_count += 1
    #     else:
    #         return False
    # return upper_count == 0 or lower_count == 0

    # Solution 2:
    # if len(dict) == 0:
    #     return False
    # upper_keys = [key for key in dict if type(key) is str and key.isupper()]
    # lower_keys = [key for key in dict if type(key) is str and key.islower()]
    # return len(upper_keys) == 0 or len(lower_keys) == 0

    # Solution 3:
    if len(dict) == 0:
        return False
    for key in dict:
        if type(key) is not str:
            return False
    lower_keys = [key for key in dict if key.islower()]
    upper_keys = [key for key in dict if key.isupper()]
    return len(upper_keys) == 0 or len(lower_keys) == 0

