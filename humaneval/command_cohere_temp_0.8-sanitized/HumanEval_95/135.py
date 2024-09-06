def check_dict_case(dictn):
    test = True 
    if not dictn:
        return False
    for key in dictn:
        if type(key) != str:
            test = False
            break
        elif key.isupper() and any(char.islower() for char in key):
            test = False
            break
        elif key.islower() and any(char.isupper() for char in key):
            test = False
            break
    return test