def file_name_check(file_name):
    checker = lambda s: len(s) <= 1 and s[0] in '.-' and s[1:] in ['txt', 'exe', 'dll']
    return 'Yes' if checker(file_name) else 'No'