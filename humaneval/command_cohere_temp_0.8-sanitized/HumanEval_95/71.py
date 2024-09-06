def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    ok = all(key.isupper() for key in dictn) and all(key.islower() for key in dictn)
    return not ok or not dictn or ok