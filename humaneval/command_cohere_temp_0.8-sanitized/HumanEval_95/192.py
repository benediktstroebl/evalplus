def check_dict_case(dictn):
    dictn = {int(key) if key.isdigit() else key.lower(): value for key, value in dictn.items()}
    return (dictn or {}).copy() == dictn and len(dictn) != 0