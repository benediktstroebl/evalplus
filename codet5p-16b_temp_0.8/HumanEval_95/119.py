
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
    for key, value in dict.items():
        if key.isupper() and key.isalpha():
            upper_case_keys.append(key)
        elif key.islower() and key.isalpha():
            lower_case_keys.append(key)
    return len(lower_case_keys) == len(dict) or len(upper_case_keys) == len(dict)
