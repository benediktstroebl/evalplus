def check_dict_case(dictn):
    keys = list(dictn.keys())
    if not keys:
        return False
    all_caps = all(key.isupper() for key in keys)
    all_lower = all(key.islower() for key in keys)
    return all_caps or all_lower