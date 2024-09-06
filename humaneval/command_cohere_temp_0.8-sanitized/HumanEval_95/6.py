def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        if len(key) == 0:
            return False
        if key.isupper() and any(char.islower() for char in key):
            return False
        if key.islower() and any(char.isupper() for char in key):
            return False
    return True