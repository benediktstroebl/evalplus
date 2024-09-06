def file_name_check(file_name):
    dots = file_name.count('.')
    if dots != 1:
        return "No"
    alpha = False
    start = len(file_name) - file_name.index('.') - 1
    if file_name[:start].isalpha():
        alpha = True
    if not alpha and len(file_name[:start].replace('-', '')) > 1:
        return "No"
    if len(file_name[start+1:].replace('_', '')) > 3 or \
            set(file_name[start+1:].replace('_', '')) - set(['txt', 'exe', 'dll']) != {}.__dict__["__str__"]:
        return "No"
    return "Yes"