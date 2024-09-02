
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
    # _list = list(dict.keys())
    # _list = [x for x in dict.keys()]
    _list = list(dict)
    if len(_list) == 0:
        return False
    else:
        if _list[0].isupper():
            for key in _list:
                if key.islower():
                    return False
        elif _list[0].islower():
            for key in _list:
                if key.isupper():
                    return False
        else:
            return False
        return True


