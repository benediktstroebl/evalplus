def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if not isinstance(key, (int, float))}
    return all(key.isupper() for key in dictn) or all(key.islower() for key in dictn) and not len(dictn)==0