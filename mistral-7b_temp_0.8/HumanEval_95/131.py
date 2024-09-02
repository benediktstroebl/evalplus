
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
    dict_case = dict.keys()
    if len(dict_case) > 0:
        if len(dict_case) == len(set(dict_case)):
            if all(d.isupper() for d in dict_case):
                return True
            elif all(d.islower() for d in dict_case):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
