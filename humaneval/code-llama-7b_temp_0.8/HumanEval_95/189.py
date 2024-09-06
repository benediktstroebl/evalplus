
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
    if len(dict) == 1:
        return True
    check_list = []
    for k in dict:
        if not isinstance(k, str):
            return False
        if len(k) == 0:
            return False
        check_list.append(k)
    if check_list[0].islower():
        for l in check_list:
            if not l.islower():
                return False
    elif check_list[0].isupper():
        for l in check_list:
            if not l.isupper():
                return False
    return True

