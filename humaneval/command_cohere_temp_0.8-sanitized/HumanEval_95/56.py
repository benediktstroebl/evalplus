def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        if dictn[key].isupper() != key.isupper():
            return False
    return True