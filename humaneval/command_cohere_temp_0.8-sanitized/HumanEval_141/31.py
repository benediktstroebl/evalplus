def file_name_check(file_name):
    lute = []
    if not file_name.isalpha():
        return "No"
    if '.' not in file_name:
        return "No"
    if len(file_name.split('.')) < 2:
        return "No"
    a = file_name.split('.')
    if len(a[0]) == 0:
        return "No"
    if len(a[0]) > 1 and not a[0][1:].isalpha():
        return "No"
    try:
        num_check = len(a[0]) >= 1 and len(a[0]) <= 3
    except Exception as e:
        return "No"
    if not num_check:
        return "No"
    b = a[1]
    if b not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"