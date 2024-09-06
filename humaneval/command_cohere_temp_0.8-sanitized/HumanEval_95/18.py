def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        if not key.isupper() and not key.islower():
            return False
    return True