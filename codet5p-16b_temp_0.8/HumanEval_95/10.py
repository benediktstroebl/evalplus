
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

    if len(dict) == 0:
        return False
    else:
        keys_lower = []
        keys_upper = []
        for key in dict:
            if key.isupper() == True:
                keys_upper.append(key)
            else:
                keys_lower.append(key)
        if len(keys_upper) == len(dict):
            return True
        elif len(keys_upper) == 0:
            return True
        else:
            return False
