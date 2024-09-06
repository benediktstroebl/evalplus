def check_dict_case(dictn):
    test = True
    if not dictn:
        return False
    for key in dictn:
        if type(key) != str:
            return False
        if len(key) > 1 and key.lower() != key and key.upper() != key:
            return False
    return test