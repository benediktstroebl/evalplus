
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

    # list of keys
    keys = list(dict.keys())
    # list of values
    values = list(dict.values())
    # condition for all key to be in lower case
    condition_1 = all(key.islower() for key in keys)
    # condition for all key to be in upper case
    condition_2 = all(key.isupper() for key in keys)
    # check if keys are all lower case or all upper case
    if condition_1 or condition_2:
        return True
    # return false if none of the conditions is true
    return False

