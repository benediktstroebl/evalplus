def check_dict_case(dict):
    if not dict:
        return False
    for key in dict:
        # check if all the keys are in lower case
        if not isinstance(key, str) or not key.islower():
            return False
    return True