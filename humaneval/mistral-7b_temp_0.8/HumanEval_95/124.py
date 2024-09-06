
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
    # TODO: Implement this function.
    # Use the assert statement below to test your function

    # list of all the keys
    keys = dict.keys()

    # lower case check
    lower_case_keys = True
    for key in keys:
        if not key.lower() == key:
            lower_case_keys = False
    # upper case check
    upper_case_keys = True
    for key in keys:
        if not key.upper() == key:
            upper_case_keys = False
    # if one is true, and the other is false, they are not the same
    if lower_case_keys is True and upper_case_keys is False:
        return True
    if lower_case_keys is False and upper_case_keys is True:
        return True
    if lower_case_keys is False and upper_case_keys is False:
        return False

