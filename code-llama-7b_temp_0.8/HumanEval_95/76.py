
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
    # (bool, str)
    def is_string(x):
        return type(x) == str

    def is_lower_case(x):
        return x.islower()

    def is_upper_case(x):
        return x.isupper()

    def is_letter(x):
        return is_string(x) and x.isalpha()

    case = None
    for key in dict:
        if not is_letter(key):
            return False
        if case == None:
            case = is_lower_case(key)
        else:
            if is_lower_case(key) != case:
                return False
    return True
