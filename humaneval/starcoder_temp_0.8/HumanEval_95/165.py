
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
    if dict == {}:
        return False
    else:
        first_key = list(dict.keys())[0]
        if isinstance(first_key, int):
            return False
        elif isinstance(first_key, str):
            first_key = first_key.lower()
            for key in dict:
                if key == first_key:
                    pass
                else:
                    key = key.lower()
                    if key!= first_key:
                        return False
                return True
