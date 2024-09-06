def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    list1 = [key.islower() for key in dictn]
    list2 = [key.isupper() for key in dictn]
    if len(dictn) == 0 or (all(list1) or all(list2)):
        return True
    else:
        return False