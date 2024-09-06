
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

    # Count the number of upper case keys.
    upper_case = 0
    lower_case = 0

    for k, v in dict.items():
        if isinstance(k, str):
            if k.isupper():
                upper_case += 1
            elif k.islower():
                lower_case += 1

    # If all keys are lower case or upper case return True.
    # If any key is upper or lower mixed return False.
    if lower_case == len(dict) or upper_case == len(dict):
        return True
    else:
        return False

