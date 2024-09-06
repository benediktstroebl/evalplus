def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or not isinstance(dictn, dict):
        return False
    lowercase_keys = all(isinstance(k, str) and k.islower() for k in dictn)
    uppercase_keys = all(isinstance(k, str) and k.isupper() for k in dictn)
    return lowercase_keys or uppercase_keys