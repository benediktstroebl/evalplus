def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dict or not all(isinstance(key, str) for key in dict):
        return False

    # Check if all keys are lowercase
    if all(key.islower() for key in dict):
        return True
    
    # Check if all keys are uppercase
    if all(key.isupper() for key in dict):
        return True
    
    return False