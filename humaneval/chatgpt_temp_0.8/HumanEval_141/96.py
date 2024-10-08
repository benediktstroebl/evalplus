def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    dot_index = -1
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits_count += 1
        elif file_name[i] == '.':
            dot_count += 1
            dot_index = i
    if digits_count > 3 or dot_count != 1:
        return 'No'
    if dot_index == 0 or dot_index == len(file_name) - 1:
        return 'No'
    if not file_name[:dot_index].isalpha() or file_name[:dot_index][0].isdigit():
        return 'No'
    if file_name[dot_index+1:] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
