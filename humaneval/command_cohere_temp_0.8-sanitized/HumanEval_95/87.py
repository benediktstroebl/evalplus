def check_dict_case(dict):
    keys = list(dict.keys())
    if len(dict) == 0 or (len(set(keys)) == 1 and isinstance(dict, dict)):
        return True 
    return False