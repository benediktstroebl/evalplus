def check_dict_case(dict):
    if not dict:
        return False
    # Check if all keys are lowercase
    if all(isinstance(k, str) and k.islower() for k in dict):
        return True
    # Check if all keys are uppercase
    if all(isinstance(k, str) and k.isupper() for k in dict):
        return True
    return False