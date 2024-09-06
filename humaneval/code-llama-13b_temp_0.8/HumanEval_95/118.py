
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
    if not dict:
        return False
    # The first key is in lower case.
    if dict[list(dict.keys())[0]].islower():
        # Check whether all keys are lower case.
        return all(map(lambda x:x.islower(), dict.keys()))
    # The first key is in upper case.
    elif dict[list(dict.keys())[0]].isupper():
        # Check whether all keys are upper case.
        return all(map(lambda x:x.isupper(), dict.keys()))
    else:
        return False
