def check_dict_case(dict):
    keys = list(dict.keys())
    if not keys:
        return False
    all_upper = all(isinstance(key, str) and key.isupper() for key in keys)
    all_lower = all(isinstance(key, str) and key.islower() for key in keys)
    return all_upper or all_lower