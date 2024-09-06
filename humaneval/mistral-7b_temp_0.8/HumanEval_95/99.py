
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
    keylist = list(dict.keys())
    if len(keylist) == 0:
        return False
    elif len(keylist) > 0:
        if dict.values() == []:
            return False
        else:
            if all(c.isupper() for c in keylist):
                return True
            elif all(c.islower() for c in keylist):
                return True
            else:
                return False
