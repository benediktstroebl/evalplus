def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    dictn = {key: val for key, val in dictn.items() if key == key.lower()}
    return len(dictn) <= 1 and len(dictn) <= 1 and not bool(dictn) or dictn