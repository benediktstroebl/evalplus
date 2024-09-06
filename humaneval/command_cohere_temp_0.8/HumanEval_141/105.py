```python
def file_name_check(file_name):
    checker = []
    
    # Checking for more than three digits in the file's name
    digits_check = len(file_name.replace('.', '').replace('\\', '').replace('|', '').replace('*', '').replace('?', '').replace('^', '').replace('~', '').replace('"', '').replace('<', '').replace('>', '').replace('\\', '').replace('/', '').replace('|', '').replace('_', '').replace('$', '').replace('&', '').replace('`', '').replace('{', '').replace('}', '').replace('|', '').replace('\\', '').replace('/', '').replace('_', '').replace('$', '').replace('&', '').replace('`', '').replace('{', '').replace('}', '').replace('~', '').replace('^', '').replace('?', '').replace('*', '').replace('`', '').replace('\\', '').replace('/', '').replace('|', '').replace('_', '').replace('$', '').replace('&', '').replace('<', '').replace('>', '').replace('\"', '').replace('{', '').replace('}', '').replace('\\', '').replace('/', '').replace('_', '').replace('$', '').replace('&', '').replace('<', '').replace('>', '').replace('~', '').replace('^', '').replace('?', '').replace('*', '').replace('`', '').replace('/', '').replace('|', '').replace('_', '').replace('$', '').replace('&', '') != '' and len(file_name.replace('.', '').replace('\\', '').replace('|', '').replace('*', '').replace('?', '').replace('^', '').replace('~', '').replace('"', '').replace('<', '').replace('>', '').replace('\\', '').replace('/', '').replace('|', '').replace('_', '').replace('$', '').replace('&', '').replace('`', '').replace('{', '').replace('}', '').replace('|', '').replace('\\', '').replace('/', '').replace('_', '').replace('$', '').replace('&', '').replace('<', '').replace('>', '').replace('\"', '').replace('{', '').replace('}', '').replace('\\', '').replace('/', '').replace('_', '').replace('$', '').replace('&', '') > 3:
        return "No"
    
    # Checking for exactly one dot in the file's name
    if len(file_name.split('.')) != 2:
        return "No"
    
    # Checking for a valid substring before the dot, and valid substring after the dot
    checker.append(file_name.split('.')[0].lower() != '')
    checker.append(file_name.split('.')[0].lower().startswith(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')) )
    checker.append(set(file_name.split('.')[1].upper() if file_name.split('.')[1].isalpha() else file_name.split('.')[1])