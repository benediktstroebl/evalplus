
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

    check_upper = False
    check_lower = False

    for key in dict.keys():
        if key.isupper():
            check_upper = True
            if key.islower():
                return False
        elif key.islower():
            check_lower = True
            if key.isupper():
                return False
        elif type(key) != str:
            return False

    if check_upper and check_lower:
        return True
    else:
        return False

