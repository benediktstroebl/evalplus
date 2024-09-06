def check_dict_case(dictn):
    dictn = {key:value for key,value in dictn.items() if isinstance(key, str)}
    ok = True
    if dictn:
        ok = all(key.isupper() for key in dictn) or all(key.islower() for key in dictn)
    return ok and not len(dictn) == 0