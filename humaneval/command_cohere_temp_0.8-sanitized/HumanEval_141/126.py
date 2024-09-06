def file_name_check(file_name):
    conditions = [
        f.startswith(str(sum(char.isdigit() for char in file_name if char != '.' and char != '/' and char != '_')) < 3),
        len(file_name.split('.')) == 2,
        file_name.split('.')[0].startswith(tuple('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')),
        set(file_name.split('.')[1]) == set(['txt', 'exe', 'dll'])
    ]
    return 'Yes' if all(conditions) else 'No'