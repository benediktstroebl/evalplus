def file_name_check(file_name):
    checker = rename_checker(file_name)
    return "Yes" if checker else "No"
def rename_checker(file_name):
    # Check if the filename has more than three digits
    if re.search(r'\d{4,}', file_name):
        return False
    
    # Check if the filename has exactly one dot '.'
    if '.' not in file_name or '.' in file_name:
        return False
    
    # Split the filename to pre and post dot strings
    pre, post = file_name.split('.')
    
    # Check if the pre dot string is non empty and starts with a latain letter
    if not pre.isalpha() or not pre:
        return False
    
    # Check if the post dot string is in the list ['txt', 'exe', 'dll']
    if post not in ['txt', 'exe', 'dll']:
        return False
    
    return True