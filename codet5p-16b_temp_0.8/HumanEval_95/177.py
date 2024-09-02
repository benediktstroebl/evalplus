
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

    if len(dict) == 0:
        return False
    l = [i for i in dict if type(i) == int]
    if len(l) > 0:
        return False
    keys = [i for i in dict]
    lower = [i for i in keys if i.islower()]
    upper = [i for i in keys if i.isupper()]
    if len(lower) == len(keys) or len(upper) == len(keys):
        return True
    return False
    
