
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
    if len(dict) > 0:
        lower_case = True
        upper_case = True
        for key, value in dict.items():
            if not key.isupper() and not key.islower():
                lower_case = False
            if not key.isupper() and not key.islower():
                upper_case = False
        if lower_case and upper_case:
            return False
        elif lower_case and not upper_case:
            return True
        else:
            return False
