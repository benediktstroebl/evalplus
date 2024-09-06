def check_dict_case(dict):
    if not dict:
        return False
    for key in dict.keys():
        # Check if all keys are lowercase or uppercase
        if not (key.isupper() or key.islower()):
            return False
    return True