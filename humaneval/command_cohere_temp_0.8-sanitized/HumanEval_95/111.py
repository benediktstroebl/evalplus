def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or not isinstance(dictn, dict):
        return False
    lowercase_dict = {key: val for key, val in dictn.items() if key == key.lower()}
    uppercase_dict = {key: val for key, val in dictn.items() if key == key.upper()}
    if len(dictn) == len(lowercase_dict) or len(dictn) == len(uppercase_dict):
        return True
    else:
        return False