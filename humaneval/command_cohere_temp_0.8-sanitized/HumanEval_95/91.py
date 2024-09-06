def check_dict_case(dictn):
    dictn = {key:value for key,value in dictn.items() if isinstance(key, str)}
    test = all(key.islower() for key in dictn) or all(key.isupper() for key in dictn)
    return not test or not dictn