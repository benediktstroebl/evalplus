
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

    # Check for empty dict
    if dict == {}:
        return False

    # Check if all keys are lowercase
    check1 = all(isinstance(k, str) and k.islower() for k in dict)

    # Check if all keys are uppercase
    check2 = all(isinstance(k, str) and k.isupper() for k in dict)

    # Return True if either check1 or check2 is True
    return check1 or check2
