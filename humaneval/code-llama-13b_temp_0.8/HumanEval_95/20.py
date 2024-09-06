
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
    # return True if empty dictionary
    if not dict:
        return True

    # initializing key_case as lower to check if the dict has all lower case keys
    key_case = 'lower'

    for k in dict:
        if k.isupper():
            # if there is a key in upper case and key_case is lower, return False
            if key_case == 'lower':
                return False
            # else set key_case as upper
            key_case = 'upper'
        elif k.islower():
            # if there is a key in lower case and key_case is upper, return False
            if key_case == 'upper':
                return False
        else:
            # if key is not in upper or lower case, return False
            return False
    return True


