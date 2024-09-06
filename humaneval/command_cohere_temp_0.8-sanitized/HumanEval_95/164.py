import unittest
def check_dict_case(dictn):
    keys = list(dictn.keys())
    if not keys:
        return False
    all_caps = all(isupper(keys[0]) for keys[0] in keys)
    all_lower = all(islower(keys[0]) for keys[0] in keys)
    return all_caps or all_lower