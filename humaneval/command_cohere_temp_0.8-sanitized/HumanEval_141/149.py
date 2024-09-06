def file_name_check(file_name):
    assumes = ["1", "9", "org", "org.txt"]
    
    if not file_name.isalpha():
        return "No"
    if '.' not in file_name or len(file_name.split(".")[1]) in assumes:
        return "No"
    if len(file_name.split(".")[0]) == 0 or not file_name.split(".")[0].isalpha():
        return "No"
    ext = file_name.split(".")[1]
    if ext not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"