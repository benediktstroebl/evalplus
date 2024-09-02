
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
    lower_case_keys = []
    upper_case_keys = []
    for k,v in dict.items():
        if isinstance(k, str):
            if k.islower():
                lower_case_keys.append(k)
            if k.isupper():
                upper_case_keys.append(k)

    if lower_case_keys == list(dict.keys()) or upper_case_keys == list(dict.keys()):
        return True
    else:
        return False

