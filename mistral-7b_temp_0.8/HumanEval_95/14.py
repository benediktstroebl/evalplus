
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

    # Make a list of keys in the dict
    keys = list(dict.keys())
    # If the dict is empty, return False
    if not keys:
        return False
    # For each key, check if it's uppercase or lowercase
    for key in keys:
        # If any key is not a string or is not all uppercase or all lowercase, return False
        if not isinstance(key, str) or key.isupper() != key.islower():
            return False
    # If we made it this far, all keys are either all uppercase or all lowercase, so return True
    return True

