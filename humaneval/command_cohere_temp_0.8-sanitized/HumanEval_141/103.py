def file_name_check(file_name):
    dig_count = file_name.count('0123456789')
    dot_count = file_name.count('.')
    
    if dot_count == 1 and dig_count <= 3 and len(file_name) > 1:
        pre, ext = file_name.split('.')
        if len(pre) > 0 and pre[0].isalpha() and ext in ['txt', 'exe', 'dll']:
            return 'Yes'
    return 'No'