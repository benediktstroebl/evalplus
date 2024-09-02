
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
    low_case = 0
    up_case = 0
    for key in dict:
        if isinstance(key, str) and key.isupper():
            up_case += 1
        elif isinstance(key, str) and key.islower():
            low_case += 1
    if low_case > 0 and up_case > 0:
        return False
    if low_case == 0:
        return True
    if up_case == 0:
        return True
    return False

