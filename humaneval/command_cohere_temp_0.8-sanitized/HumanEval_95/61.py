def check_dict_case(dictn):
    dictn = {int(key) if isinstance(key, str) and key.isupper() else key for key in dictn.keys()}
    return len(dictn) == len(set(dictn)) and not dictn or all(isinstance(key, str) and key.islower() for key in dictn)