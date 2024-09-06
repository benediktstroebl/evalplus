
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

    # Code here
    if dict == {}:
        return False
    elif len(list(dict.keys())) == 1:
        if isinstance(list(dict.keys())[0], str):
            return True
        else:
            return False
    else:
        key_list = list(dict.keys())
        first_key = key_list[0]
        case_1 = [isinstance(first_key, str), all(isinstance(key, str) for key in key_list)]
        case_2 = [isinstance(first_key, str), all(isinstance(key, str) for key in key_list)]
        if (case_1[0] == case_1[1]) or (case_2[0] == case_2[1]):
            return False
        else:
            return True
