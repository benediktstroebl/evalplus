
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

    def is_lower_case(s):
        return all(c.islower() for c in s)

    def is_upper_case(s):
        return all(c.isupper() for c in s)

    if len(dict.keys()) == 0:
        return False

    if len(dict.keys()) == 1:
        return True

    case = is_lower_case(dict.keys()[0])
    for key in dict.keys():
        if is_lower_case(key) != case:
            return False

    return True
