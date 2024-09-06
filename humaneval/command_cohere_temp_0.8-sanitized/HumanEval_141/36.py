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
    
    if len(file_name) == 0:
        return "File name should not be empty"
    
    if len(file_name) > 255:
        return "File name should not be longer than 255 characters"
    
    digits = '0123456789'.split('')
    if len(digits) > sum(char in digits for char in file_name):
        return "Should not be more than three digits ('0'-'9') in the file's name"
    
    dot_index = file_name.find('.')
    if dot_index < 0 or dot_index >= len(file_name)-1:
        return "The file's name contains exactly one dot '.'"
    
    pre_dot = file_name[:dot_index]
    if len(pre_dot) == 0 or not pre_dot.isalpha():
        return "The substring before the dot should not be empty, and it should start with a letter from the latin alphapet"
    
    post_dot = file_name[dot_index+1:]
    if post_dot != 'txt' and post_dot != 'exe' and post_dot != 'dll':
        return "The substring after the dot should be one of these: ['txt', 'exe', 'dll']"
    
    return "Yes"