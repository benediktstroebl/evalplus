def file_name_check(file_name):
    decimal_count = file_name.count('.')
    if decimal_count != 1:
        return "No"
    pre, ext = file_name.split(".")
    if len(pre) == 0 or not pre[0].isalpha():
        return "No"
    if ext not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"