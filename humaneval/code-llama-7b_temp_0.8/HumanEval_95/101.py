
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
    # has_lower = False
    # has_upper = False
    # for key in dict:
    #     if isinstance(key, str) and key.islower():
    #         has_lower = True
    #     if isinstance(key, str) and key.isupper():
    #         has_upper = True
    # if has_lower and has_upper:
    #     return False
    # else:
    #     return True
    # lower = []
    # upper = []
    # for key in dict:
    #     if isinstance(key, str) and key.islower():
    #         lower.append(key)
    #     elif isinstance(key, str) and key.isupper():
    #         upper.append(key)
    # if lower and upper:
    #     return False
    # return True
    # return False if dict else True
    return all(isinstance(key, str) and key.isupper() for key in dict) if dict else True
