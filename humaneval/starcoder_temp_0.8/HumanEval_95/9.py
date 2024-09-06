
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
    for key in dict:
        if type(key)!= str:
            return False
    lower_case = [i.islower() for i in list(dict.keys())]
    upper_case = [i.isupper() for i in list(dict.keys())]
    if lower_case.count(True) == len(lower_case) or upper_case.count(True) == len(upper_case):
        return True
    else:
        return False

