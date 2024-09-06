def check_dict_case(dictn):
    dictn = {int(key) if key.isnumeric() else key.lower(): value for key, value in dictn.items()}
    return len(dictn) <= 1 and all(key in dictn.values() or key == key.upper() for key in dictn)