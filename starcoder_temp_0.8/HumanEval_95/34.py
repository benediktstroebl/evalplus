
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
    elif not isinstance(dict, dict):
        raise TypeError('Expected a dict')

    for k in dict.keys():
        if not isinstance(k, str):
            raise TypeError('Expected a dict with keys that are strings')

    first_element = list(dict.keys())[0]
    if not first_element.islower():
        return False
    elif not first_element.isupper():
        return False
    else:
        return all(k.islower() or k.isupper() for k in dict.keys())
