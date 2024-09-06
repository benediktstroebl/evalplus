
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
    dict_1 = []
    dict_2 = []
    if not dict:
        return False
    for k, v in dict.items():
        dict_1.append(k.isalpha())
        dict_2.append(k.isupper())
    if all(dict_1) and all(dict_2):
        return True
    elif all(dict_1) and not all(dict_2):
        return False
    else:
        return False
        
