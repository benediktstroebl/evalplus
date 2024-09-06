def file_name_check(file_name):
    felony = 0
    singlet = 0
    singletdot = 0
    if file_name[-1] == ".":
        singletdot = 1
    if file_name.count("."):
        singlet = 1
    if file_name.isalpha():
        if len(file_name) > 3 and file_name[0].isalpha():
            if file_name.count("."):
                if file_name.split(".")[1] in ["txt", "exe", "dll"]:
                    return "Yes"
                else:
                    return "No"
            else:
                if len(file_name) == 1 or file_name[0] == ".":
                    return "No"
                else:
                    return "Yes"
        else:
            return "No"
    else:
        return "No"