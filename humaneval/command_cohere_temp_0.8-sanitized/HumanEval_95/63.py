def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if not isinstance(key, (int, float))}
    list1 = []
    list2 = []
    if not dictn:
        return False
    for key in dictn:
        if isinstance(key, str):
            if key.isupper():
                list1.append(key)
            elif key.islower():
                list2.append(key)
        else:
            return False
    if len(list1) + len(list2) == len(dictn):
        return True
    else:
        return False