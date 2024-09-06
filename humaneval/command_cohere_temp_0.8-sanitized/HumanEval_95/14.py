def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dict or not all(isinstance(key, str) for key in dict):
        return False
    # Check if all keys are lowercase
    lowercase_dict = {key: val for key, val in dict.items()}
    lowercase_keys = lowercase_dict.keys()
    return lowercase_keys.isupper() or lowercase_keys.islower()