def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    if all(isinstance(key, str) and (key.isupper() or key.islower()) for key in keys):
        return True
    return False