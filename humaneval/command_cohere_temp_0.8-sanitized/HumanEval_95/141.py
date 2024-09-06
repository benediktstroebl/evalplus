def check_dict_case(dictn):
    dictn = {int(key) if isinstance(key, str) and key.isupper() else key: value for key, value in dictn.items()}
    return len(dictn) == 0 or all(isinstance(key, str) and (key.islower() or key.isupper()) for key in dictn)