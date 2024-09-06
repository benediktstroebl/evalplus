def check_dict_case(dictn):
    keys = list(dictn.keys())
    if not keys:
        return False
    all_upper = all(isinstance(k, str) and k.isupper() for k in keys)
    all_lower = all(isinstance(k, str) and k.islower() for k in keys)
    return all_upper or all_lower