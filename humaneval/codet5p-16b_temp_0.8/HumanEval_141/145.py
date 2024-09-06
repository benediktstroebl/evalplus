
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

    if not file_name[-4:] in ['txt', 'exe', 'dll']:
        return 'No'
    
    digits = 0
    for char in file_name:
        if char in '123456789':
            digits += 1
        else:
            break
    
    if digits > 3:
        return 'No'
    
    if '.' not in file_name:
        return 'No'
    
    file_name = file_name.split('.')
    file_name = file_name[0]
    
    if not file_name[0].isalpha():
        return 'No'
    
    if not file_name.lower()[0].isalpha():
        return 'No'
    
    return 'Yes'
