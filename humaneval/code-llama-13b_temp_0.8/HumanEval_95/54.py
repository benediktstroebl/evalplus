
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

    # init case
    lc = True
    uc = True

    for k in dict:
        if not isinstance(k, str):
            return False
        
        # if all keys are in lowercase, then lc = True
        if k.islower():
            lc = True
        else:
            lc = False
        
        # if all keys are in uppercase, then uc = True
        if k.isupper():
            uc = True
        else:
            uc = False

    # if lc or uc is True, then return True
    if lc or uc:
        return True
    else:
        return False

