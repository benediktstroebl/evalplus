
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
    
    # check if dict is empty
    if len(dict) == 0:
        return False

    # get a list of the keys of the dict
    keys = dict.keys()

    # check if all keys are in lower case
    if all(k.islower() for k in keys):
        return True
    # check if all keys are in upper case
    if all(k.isupper() for k in keys):
        return True

    return False
