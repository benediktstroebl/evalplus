
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

    # If it's empty, return False
    if len(dict) == 0:
        return False

    # Get the first key
    first = dict.keys()[0]
    # Get the last key
    last = dict.keys()[-1]
    # If they're different, return False
    if type(first) is not type(last):
        return False
    # Else, check that they're both lower or upper case
    return first.isupper() == last.isupper()
