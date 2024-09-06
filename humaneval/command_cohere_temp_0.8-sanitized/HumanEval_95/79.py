def check_dict_case(dict):
    if not dict:
        return False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.isupper() and any(c.islower() for c in key):
            return False
        if key.islower() and any(c.isupper() for c in key):
            return False
    return True