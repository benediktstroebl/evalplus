def check_dict_case(dictn):
    keys = dict().keys()
    if not keys:
        return False
    if all(isinstance(key, str) and (key.isupper() or key.islower()) for key in keys):
        return True
    return False