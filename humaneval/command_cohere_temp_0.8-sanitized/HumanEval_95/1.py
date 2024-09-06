def check_dict_case(dictn):
    dictn = {int(key) if key.isdigit() else key: value for key, value in dictn.items()}
    return len(dictn) <= 1 and all(dictn[key].islower() if dictn[key] else key.isupper() for key in dictn)