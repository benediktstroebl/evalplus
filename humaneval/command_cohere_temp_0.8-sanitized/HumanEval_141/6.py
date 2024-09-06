def file_name_check(file_name):
    dots = file_name.count('.')
    if dots != 1:
        return "No"
    pre, ext = file_name.split('.')
    if len(pre) == 0 or not pre[0].isalpha():
        return "No"
    if len(ext) > 3 or not ext.isalpha():
        return "No"
    ext = ext.lower()
    if ext not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"