def check_dict_case(dict):
    keys = list(dict.keys())
    if not keys:
        return False
    all_caps = all(k.isupper() for k in keys)
    all_lower = all(k.islower() for k in keys)
    return all_caps or all_lower