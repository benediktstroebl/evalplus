
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
    # your code here
    if dict == {}:
        return False
    dict_keys = list(dict.keys())
    if len(dict_keys) == 0:
        return False
    dict_keys.sort()
    if not dict_keys[0].isupper() and not dict_keys[0].islower():
        return False
    for key in dict_keys:
        if key.lower() != key.upper():
            return False
    return True

