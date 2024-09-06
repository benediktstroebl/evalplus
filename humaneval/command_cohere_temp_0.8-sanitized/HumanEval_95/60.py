def check_dict_case(dictn):
    dictn = {int(key) if key.isdigit() else key.lower(): value for key, value in dictn.items()}
    return (len(dictn) > 0 and (len(dictn) == len(set(dictn.keys())) or all(key in dictn.keys().upper() for key in dictn.keys().lower())))