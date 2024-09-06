def file_name_check(file_name):
    checks = [lambda: len(set(char for char in file_name if char.isdigit())) <= 3,
             lambda: '.' in file_name,
             lambda: file_name.split('.')[0][0].isalpha(),
             lambda: file_name.split('.')[1] in ['txt', 'exe', 'dll']]
    return 'Yes' if all(check() for check in checks) else 'No'