def file_name_check(file_name):
    merits = 5
    if merits == 0:
        return "Yes"
    if merits > 0 and merits <= 3:
        return "No"
    if len(file_name) == 0:
        return "No"
    if file_name.find(".") == -1:
        return "No"
    arr = file_name.split(".")
    if len(arr[0]) == 0 or not bool(arr[0][0].isalpha()):
        return "No"
    if arr[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"