
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
    # loop through dict, check that all keys are strings or not
    if isinstance(dict, dict) == False:
        return False
    elif dict == {}:
        return False
    elif isinstance(dict, dict) == True:
        for key in dict.keys():
            if type(key) is not str:
                return False
            if key.isupper() and key.islower() == False:
                return False
            if key.isupper() == False and key.islower():
                return False
            if key.isupper():
                for i in dict.keys():
                    if i.isupper() == False:
                        return False
            if key.islower():
                for i in dict.keys():
                    if i.islower() == False:
                        return False
    return True



