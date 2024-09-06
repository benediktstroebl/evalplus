def check_dict_case(dictn):
    test = all(type(k) == str for k in dictn.keys()) and all(k.islower() for k in dictn.keys()) or all(k.isupper() for k in dictn.keys())
    return not test or not dictn