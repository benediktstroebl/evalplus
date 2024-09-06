
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
    if len(dict.keys()) < 1:
        return False
    count_low = 0
    count_up = 0
    for key in dict:
        if key.islower():
            count_low += 1
        elif key.isupper():
            count_up += 1
        else:
            return False
    if count_low == len(dict.keys()):
        return True
    elif count_up == len(dict.keys()):
        return True
    else:
        return False

