def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or len(dictn) != len(set(dictn.keys())):
        return False
    dictn_up = {k.upper(): dictn[k] for k in dictn}
    dictn_lo = {k.lower(): dictn[k] for k in dictn}
    return dictn == dictn_up or dictn == dictn_lo