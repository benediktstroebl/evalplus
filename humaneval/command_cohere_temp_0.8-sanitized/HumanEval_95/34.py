def check_dict_case(dictn):
    dictn = {int(key) if isinstance(key, str) and key.isalpha() else key: value for key, value in dictn.items()}
    return len(dictn) <= 1 and all(dictn.values()) and all(dictn.keys())