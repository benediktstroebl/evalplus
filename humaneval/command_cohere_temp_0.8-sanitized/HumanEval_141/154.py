def file_name_check(file_name):
    alphapet_check = bool(re.match(r'[a-zA-Z]\w*', file_name))
    digit_check = '-' not in file_name and file_name.lower() not in '1234567890' and file_name.lower() not in '9876543210' 
    dot_check = len(file_name.split('.')) == 2
    extension_check = file_name.split('.')[-1].lower() in ['txt', 'exe', 'dll']
    return 'Yes' if alphapet_check and digit_check and dot_check and extension_check else 'No'