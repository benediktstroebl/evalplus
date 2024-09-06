
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

    result = False
    if not dict:
        return result
    all_keys = dict.keys()
    all_keys = list(all_keys)
    if not all_keys:
        return result
    all_keys_lower = [i.lower() for i in all_keys]
    all_keys_upper = [i.upper() for i in all_keys]
    if all_keys_lower == all_keys_upper:
        result = True
    return result

