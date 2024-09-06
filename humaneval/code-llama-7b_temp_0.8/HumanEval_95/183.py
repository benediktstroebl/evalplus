
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
    # check for empty dictionary
    if not dict:
        return False
    # check if there is a mix of lower case and upper case strings
    is_lower_case = True
    is_upper_case = True
    for key in dict:
        if isinstance(key, str):
            if key.islower() == False:
                is_lower_case = False
            if key.isupper() == False:
                is_upper_case = False
    if is_lower_case == False and is_upper_case == False:
        return False
    return True
