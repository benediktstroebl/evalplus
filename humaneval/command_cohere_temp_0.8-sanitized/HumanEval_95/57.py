def check_dict_case(dict):
    if not dict:
        return False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.isupper() and len(key) != len(key.lower()):
            return False
        if key.islower() and len(key) != len(key.upper()):
            return False
    return True