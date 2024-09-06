
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
    
    # this returns the keys as a list
    keys = list(dict.keys())
    # if there are no keys return False
    if len(keys) == 0:
        return False
    # lowercase for the first key
    l = keys[0].islower()
    
    # check the rest of the keys
    for key in keys:
        # check if they are all lowercase or uppercase
        # if they are not the same return False
        if key.islower()!= l:
            return False
    # if we got here all keys are either lowercase or uppercase
    # and they are all equal
    return True
    

