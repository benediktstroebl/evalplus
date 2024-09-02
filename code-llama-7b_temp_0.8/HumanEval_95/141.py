
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

    # One liner
    # return all(isinstance(key, str) and key.islower() for key in dict) if dict else False

    # My solution
    if dict == None or dict == {} or dict == {}:
        return False

    is_lower = True
    is_upper = True

    for key in dict:
        is_lower = is_lower and isinstance(key, str) and key.islower()
        is_upper = is_upper and isinstance(key, str) and key.isupper()

    return is_lower or is_upper
