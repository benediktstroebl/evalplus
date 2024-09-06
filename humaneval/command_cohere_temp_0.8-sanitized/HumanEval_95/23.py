def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    # Check if all keys are lowercase
    if all(isinstance(key, str) and key.islower() for key in keys):
        return True
    # Check if all keys are uppercase
    if all(isinstance(key, str) and key.isupper() for key in keys):
        return True
    return False