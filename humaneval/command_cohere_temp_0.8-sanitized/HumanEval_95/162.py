def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        elif key.isupper() and any(c.islower() for c in key):
            return False
        elif key.islower() and any(c.isupper() for c in key):
            return False
    return True