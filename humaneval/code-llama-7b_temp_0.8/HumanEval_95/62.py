
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
    
    lower_case = True
    upper_case = True
    for key, value in dict.items():
        if type(key) is not str:
            return False
        if key.islower():
            lower_case = True
        else:
            lower_case = False
        if key.isupper():
            upper_case = True
        else:
            upper_case = False
        if not (lower_case or upper_case):
            return False
    return True
