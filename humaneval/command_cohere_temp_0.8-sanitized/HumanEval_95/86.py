def check_dict_case(dictn):
    dictn = {key: dictn[key] for key in dictn if isinstance(key, str)}
    ok = True
    if len(dictn) == 0:
        ok = False
    elif len(set([k.lower() for k in dictn])) == len(dictn) or len(set([k.upper() for k in dictn])) == len(dictn):
        ok = True
    else:
        ok = False
    return ok