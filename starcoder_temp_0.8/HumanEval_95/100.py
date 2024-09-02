
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
    # Your code here
    if not dict:
        return False
    for key in dict:
        if not isinstance(key, str):
            return False
    keys_list = list(dict.keys())
    if keys_list.count(keys_list[0].lower()) == len(keys_list):
        for key in dict:
            if key.lower()!= key:
                return False
        return True
    elif keys_list.count(keys_list[0].upper()) == len(keys_list):
        for key in dict:
            if key.upper()!= key:
                return False
        return True
    else:
        return False

