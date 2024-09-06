def check_dict_case(dictn):
    keys = list(dictn.keys())
    if not keys:
        return False
    all_caps = all(isupper(keys[0].lower()) for keys in keys)
    all_lower = all(islower(keys[0].lower()) for keys in keys)
    if all_caps or all_lower:
        return True
    else:
        return False