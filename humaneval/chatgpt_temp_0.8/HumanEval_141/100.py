def file_name_check(file_name):
    digits_count = 0
    for char in file_name:
        if char.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    name_parts = file_name.split('.')
    if not name_parts[0].isalpha() or name_parts[0] == '':
        return 'No'
    if name_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
