def file_name_check(file_name):
    lat_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_dot = None
    file_ext = None
    if len(file_name) == 0:
        return 'No'
    if len(file_name) > 0 and file_name[0] not in lat_alphabet:
        return 'No'
    if len(file_name) > 0 and file_name[-3:] == '.exe':
        file_ext = 'exe'
    elif len(file_name) > 0 and file_name[-3:] == '.dll':
        file_ext = 'dll'
    elif len(file_name) > 0 and file_name[-2:] == '.txt':
        file_ext = 'txt'
    for i in range(len(file_name)):
        if file_name[i] == '.':
            num_dot = i
        if file_name[i] in '0123456789':
            if num_dot is None:
                return 'No'
            elif i - num_dot - 1 > 3:
                return 'No'
    if file_ext is None:
        return 'No'
    else:
        return 'Yes'