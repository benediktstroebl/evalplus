def check_dict_case(dictn):
    dictn = {key: dictn[key] for key in dictn if isinstance(key, str)}
    return all(len(key) == len(key.lower()) for key in dictn) and not any(dictn) or all(map(str.isupper, dictn)) and not any(dictn)