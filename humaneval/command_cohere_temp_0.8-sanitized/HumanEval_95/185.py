def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or len(dictn) != len(set(dictn.keys())):
        return False
    all_caps = all(isupper(k) for k in dictn.keys())
    all_lower = all(islower(k) for k in dictn.keys())
    return all_caps or all_lower