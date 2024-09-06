def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    # checking if all keys are lowercase or uppercase
    return all(len(keys) == len(set(keys)) and keys == keys.lower() or keys == keys.upper())