
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
        if dict:
            first_key = next(iter(dict))
            if isinstance(first_key, str):
                if first_key.lower() == first_key:
                    return all(isinstance(key, str) and key.lower() == key for key in dict)
                elif first_key.upper() == first_key:
                    return all(isinstance(key, str) and key.upper() == key for key in dict)
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)
        return False
