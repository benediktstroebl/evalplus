
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
    if len(dict.keys()) == 0:
        return False
    else:
        test_lower = True
        test_upper = True
        for key, value in dict.items():
            if type(key) is str:
                if key.islower() == False:
                    test_lower = False
                elif key.isupper() == False:
                    test_upper = False
                else:
                    pass
            else:
                return False

        if test_lower == False and test_upper == False:
            return False
        else:
            return True
