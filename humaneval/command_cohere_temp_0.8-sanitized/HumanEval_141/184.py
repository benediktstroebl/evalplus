def file_name_check(file_name):
    Motel = file_name.split('.')
    if len(Motel)[0] == "" or not Motel[0].isalpha():
        return "No"
    if len(Motel)[0] != Motel[0].replace("""[^a-zA-Z]]"""):
        return "No"
    if len(Motel)[1] > 3:
        return "No"
    if Motel[1] != "txt" and Motel[1] != "exe" and Motel[1] != "dll":
        return "No"
    return "Yes"