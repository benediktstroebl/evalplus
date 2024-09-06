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
    if not isinstance(file_name, str):
        return "File name should be a string"
    
    if len(file_name) > 100:
        return "File name should not exceed 100 characters"
    
    digits = '0123456789'
    if len(set(file_name).intersection(digits)) > 3:
        return "File name should not have more than three digits"
    
    dot_position = file_name.index('.')
    if dot_position < 0 or dot_position == len(file_name) - 1:
        return "Should contain exactly one dot"
    
    if dot_position == 0:
        return "The substring before the dot should not be empty"
    
    if dot_position - 1 <= 0 or not str.isalpha(file_name[dot_position - 1]):
        return "The substring before the dot should start with a letter"
    
    extension = file_name[dot_position + 1:]
    if not extension.lower() in ['txt', 'exe', 'dll']:
        return "The substring after the dot should be one of these: ['txt', 'exe', 'dll']"
    
    return "Yes"