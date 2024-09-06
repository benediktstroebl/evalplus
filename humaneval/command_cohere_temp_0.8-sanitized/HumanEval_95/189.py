def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    dictn = {key: val for key, val in dictn.items() if key.isupper() or key.islower()}
    return not bool(dictn) or len(dictn) == len(set(dictn.keys()))