def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    list1 = []
    list2 = []
    if len(dictn) == 0:
        return False
    for key in dictn.keys():
        if len(key) > 0:
            first_char = key[0]
            rest = key[1:]
            if (first_char.isupper() and rest.islower()) or (first_char.islower() and rest.isupper()):
                list1.append(key)
            else:
                list2.append(key)
        elif key:
            list1.append(key)
    if len(list1) == len(dictn) or len(list2) == len(dictn):
        return True
    else:
        return False