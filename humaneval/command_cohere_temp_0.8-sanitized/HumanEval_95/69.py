def check_dict_case(dictn):
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
    show_keys = True
    if dictn == {}:
        return False
    for key in dictn.keys():
        if not isinstance(key, str):
            show_keys = False
            break
        if len(key) > 1 and key.isupper() != key.istitle():
            show_keys = False
            break
    if show_keys and all(key.islower() for key in dictn.keys()):
        return True
    elif not show_keys and all(key.isupper() for key in dictn.keys()):
        return True
    else:
        return False