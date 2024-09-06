def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    list1 = []
    list2 = []
    if len(dictn) == 0:
        return False
    for key in dictn.keys():
        if key.isupper() or key.islower():
            list1.append(key)
        else:
            list2.append(key)
    if len(list1) + len(list2) == 0:
        return True
    if len(list1) == len(dictn):
        return True
    if len(list2) == len(dictn):
        return True
    return False