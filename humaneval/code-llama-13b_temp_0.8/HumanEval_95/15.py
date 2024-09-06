
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
    try:
        is_lower_case = True
        is_upper_case = True

        for key in dict:
            if not isinstance(key, str):
                return False

            if key.isupper():
                is_lower_case = False
            elif key.islower():
                is_upper_case = False
            else:
                return False

        return is_lower_case or is_upper_case
    except:
        return False


