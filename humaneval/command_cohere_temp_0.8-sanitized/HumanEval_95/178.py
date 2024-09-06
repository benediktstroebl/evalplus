def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if not isinstance(key, str) or key.isupper()}
    return len(dictn) <= 1 and not dictn or all(key.islower() for key in dictn)