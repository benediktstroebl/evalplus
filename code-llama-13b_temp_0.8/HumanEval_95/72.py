
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

    case = list(dict.keys())[0][0].islower()
    for key in dict:
        if not dict[key].isupper() and not dict[key].islower():
            return False
        elif dict[key].isupper() and not case:
            return False
        elif dict[key].islower() and not case:
            return False

    return True

