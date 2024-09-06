def check_dict_case(dictn):
    keys = []
    for key in dictn.keys():
        keys.append(key)
    if len(keys) == 0:
        return False
    elif all(isinstance(key, str) and (key.isupper() or key.islower()) for key in keys):
        return True
    else:
        return False