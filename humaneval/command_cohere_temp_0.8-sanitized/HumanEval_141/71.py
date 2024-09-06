def file_name_check(file_name):
    locus, ext = file_name.split('.')
    if len(locus) == 0 or not locus[0].isalpha():
        return "No"
    if len(locus) > 3:
        return "No"
    if ext not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"