def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or not all(isinstance(key, str) for key in dictn): 
        return False 
    # check if all letters are either in lower or upper case
    return all(dictn.values()) or all(dictn.values()) == dictn