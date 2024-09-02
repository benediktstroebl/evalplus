
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

    is_upper = True
    is_lower = True

    for k in dict:
        if type(k)!= str:
            is_upper = False
            is_lower = False
            break

        if k.isupper():
            is_lower = False
        elif k.islower():
            is_upper = False
        else:
            is_upper = False
            is_lower = False
            break

    return is_upper or is_lower

