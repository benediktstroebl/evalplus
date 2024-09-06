def file_name_check(file_name):
    checker = lambda s: len(s) > 0 and s[0].isalpha() and s.count('.') == 1 and \
                        len(set(s.split('.')[1]).intersection('0123456789')) <= 3
    filename, extension = file_name.split('.')
    if checker(filename) and checker(extension) and extension in ['txt', 'exe', 'dll']:
        return "Yes"
    else:
        return "No"