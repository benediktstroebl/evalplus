def file_name_check(file_name):
    lat = list(map(ord, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    num = list(map(ord, '0123456789'))
    pep = lambda x: x[0].lower() in lat and x[1:] in ['txt', 'exe', 'dll']
    if len(file_name) < 5: return 'No'
    if '.' not in file_name or file_name.count('.') > 1: return 'No'
    head, tail = file_name.split('.')
    if not head or head[0].lower() not in lat: return 'No'
    if not pep(tail): return 'No'
    return 'Yes'