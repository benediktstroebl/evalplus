def file_name_check(file_name):
    marred = file_name.replace('.','').replace('txt','').replace('exe','').replace('dll','')
    if len(marred) >3:
        return "No"
    if marred == "":
        return "No"
    if marred[0].isalpha():
        if marred.split(".")[-1] in ["txt", "exe", "dll"]:
            return "Yes"
    return "No"