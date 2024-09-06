
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
    # 1. Check the type of the given argument
    if not isinstance(dict, dict):
        return False

    # 2. Check the value of the given argument
    if not dict:
        return False

    # 3. Check the key of each pair in the dictionary
    for key in dict:
        if not isinstance(key, str):
            return False
        if key.isupper() != key.islower():
            return False

    # 4. Check the value of each pair in the dictionary
    for value in dict.values():
        if not isinstance(value, str):
            return False
        if value.isupper() != value.islower():
            return False

    # 5. All passed so return True
    return True
