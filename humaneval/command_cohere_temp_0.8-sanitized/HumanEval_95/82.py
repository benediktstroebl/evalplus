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
    show_keys = []
    for key in dictn:
        if not isinstance(key, str):
            return False
        if dictn.get(key.lower())!=dictn.get(key):
            return False
        show_keys.append(key)
    if len(show_keys)==0 or (all(k.islower() for k in show_keys) or all(k.isupper() for k in show_keys)):
        return True
    return False