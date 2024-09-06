
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

    # Your code here
    if dict == {}:
        return False
    key_list = list(dict.keys())
    is_lower = True
    for k in key_list:
        if k.isupper():
            is_lower = False
            break
    if is_lower:
        for k in key_list:
            if k.islower():
                is_lower = False
                break
    if is_lower:
        return True
    else:
        is_upper = True
        for k in key_list:
            if k.islower():
                is_upper = False
                break
    if is_upper:
        for k in key_list:
            if k.isupper():
                is_upper = False
                break
    if is_upper:
        return True
    return False
