def check_dict_case(dictn):
    keys = dict().keys()
    if len(keys) == 0:
        return False
    elif all(type(k) == str for k in keys) and all(k.islower() or k.isupper() for k in keys):
        return True
    else:
        return False