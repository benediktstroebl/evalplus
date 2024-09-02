
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

    # initialize variables
    case = None
    first_key = None

    # get first key
    for key in dict:
        first_key = key
        break

    # check case
    if dict and isinstance(first_key, str):
        if first_key.islower():
            case = "lower"
        elif first_key.isupper():
            case = "upper"
    
    # check all other keys
    for key in dict:
        if case == "lower":
            if not key.islower():
                return False
        elif case == "upper":
            if not key.isupper():
                return False
        else:
            return False
    
    return True


