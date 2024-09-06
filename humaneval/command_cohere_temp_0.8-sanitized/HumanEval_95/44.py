def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    ok = True
    # check if all keys are lower case
    if len(dictn) > 1:
        ok &= all(key.islower() for key in dictn)
    # check if all keys are upper case
    if len(dictn) > 1:
        ok &= all(key.isupper() for key in dictn)
    if not dictn:
        ok = False
    return ok