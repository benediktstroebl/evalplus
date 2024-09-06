
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
    # If the dictionary is empty, return False
    if not dict:
        return False
    # If all the keys are lowercase, return True
    if all(key.lower() == key for key in dict):
        return True
    # If all the keys are uppercase, return True
    elif all(key.upper() == key for key in dict):
        return True
    # If any key is not lowercase or uppercase, return False
    else:
        return False
