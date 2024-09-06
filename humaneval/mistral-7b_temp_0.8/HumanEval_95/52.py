
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
    if not isinstance(dict, dict):
        raise TypeError("The argument is not a dictionary")
    if not dict:
        return False
    if len(set(dict.keys())) == 1:
        if dict.keys()[0].isupper():
            return all(k.isupper() for k in dict.keys())
        elif dict.keys()[0].islower():
            return all(k.islower() for k in dict.keys())
        else:
            return False
    else:
        return False
