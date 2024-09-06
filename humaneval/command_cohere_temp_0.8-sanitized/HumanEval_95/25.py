def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or not isinstance(dictn, dict):
        return False
    lowercase_dict = {key.lower(): value for key, value in dictn.items()}
    uppercase_dict = {key.upper(): value for key, value in dictn.items()}
    if lowercase_dict == uppercase_dict or dictn == lowercase_dict or dictn == uppercase_dict:
        return True
    else: 
        return False