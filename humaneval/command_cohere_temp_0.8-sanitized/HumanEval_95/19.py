def check_dict_case(dictn):
    dictn = {int(key) if key.isdigit() else key.lower(): value for key, value in dictn.items()}
    return len(dictn) == 0 or all(map(dictn.get, dictn.keys())) and all(map(dictn.get, dictn.keys().upper()))