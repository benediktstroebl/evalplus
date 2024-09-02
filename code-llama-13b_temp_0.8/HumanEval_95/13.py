
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

    keys = dict.keys()
    count_lower = 0
    count_upper = 0
    for key in keys:
        if isinstance(key, str) is False:
            return False
        if key.islower() is True:
            count_lower += 1
        elif key.isupper() is True:
            count_upper += 1
    return count_lower == 0 or count_upper == 0
    

