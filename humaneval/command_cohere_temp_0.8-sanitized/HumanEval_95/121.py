def check_dict_case(dictn):
    dictn = {int(key) if isinstance(key, str) else key for key in dictn.keys()}
    return len(dictn) != 0 and (all(key.isupper() for key in dictn) or all(key.islower() for key in dictn))