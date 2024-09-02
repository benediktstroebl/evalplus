
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

    # store first key value
    first = list(dict.values())[0]

    # check if dict is empty or if first key value is not string
    if not isinstance(first, str) or not isinstance(first, int):
        return False

    # check if all keys are lower case or upper case
    if all([key.islower() for key in dict.keys()]) or all([key.isupper() for key in dict.keys()]):
        return True
    
    return False
