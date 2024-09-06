
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
    # this works too
    # return bool(all(type(i) == str and i.islower() for i in dict.keys())) or bool(all(type(i) == str and i.isupper() for i in dict.keys()))

    # The following is equivalent to the return statements above.
    if len(dict) == 0:
        return False
    else:
        if type(list(dict.keys())[0]) == str:
            return all(type(i) == str and i.islower() for i in dict.keys()) or all(type(i) == str and i.isupper() for i in dict.keys())
        else:
            return False
