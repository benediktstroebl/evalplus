import unittest
def check_dict_case(dict):
    if not dict:
        return False
    for key, value in dict.items():
        if not isinstance(key, str) or not key.islower() and not key.isupper():
            return False
        if not isinstance(value, str):
            return False
    return True