def check_dict_case(dict):
    if not dict:
        return False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.isupper() and any(char.islower() for char in key):
            return False
        if key.islower() and any(char.isupper() for char in key):
            return False
    return True