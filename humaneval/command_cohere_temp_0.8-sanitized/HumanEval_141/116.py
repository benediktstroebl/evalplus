def file_name_check(file_name):
    dots = file_name.count('.')
    if dots > 1:
        return "No"
    elif dots == 1 and len(file_name) > 1 and file_name[0] != "." and file_name[0].isalpha():
        if file_name.split(".")[1] in ["txt", "exe", "dll"]:
            return "Yes"
        else:
            return "No"
    else:
        return "No"