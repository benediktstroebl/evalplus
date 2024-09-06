
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

    def is_uppercase(string):
        return string == string.upper()

    def is_lowercase(string):
        return string == string.lower()
    
    def is_string(object):
        return type(object) == str

    def check_case_of_key(key):
        return is_string(key) and (is_uppercase(key) or is_lowercase(key))

    if dict == {}:
        return False

    key_cases = [check_case_of_key(key) for key in dict.keys()]
    return False if False in key_cases else True
