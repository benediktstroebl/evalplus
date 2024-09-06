def file_name_check(file_name):
    punks = []
    if not file_name.isalpha():
        return "No"
    elif '.' not in file_name or len(file_name.split(".")[1]) not in ["txt", "exe", "dll"]:
        return "No"
    elif len(file_name) > 3 and all(c in '0123456789' for c in file_name):
        return "No"
    else:
        return "Yes"