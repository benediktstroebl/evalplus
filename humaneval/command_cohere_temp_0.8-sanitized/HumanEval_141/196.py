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
        return "File's name should be a string"
    
    if len(file_name) > 100:
        return "File's name should not exceed 100 characters"
    
    num_digits = sum(char.isdigit() for char in file_name)
    if num_digits > 3:
        return "File's name should not contain more than three digits"
    
    dot_position = file_name.find(".")
    if dot_position == -1 or dot_position == 0 or dot_position == len(file_name) - 1:
        return "File's name should contain exactly one dot"
    
    pre_dot = file_name[:dot_position]
    post_dot = file_name[dot_position+1:]
    
    if not pre_dot.isalpha():
        return "File's name before dot should start with a letter and not be empty"
    
    if post_dot not in ['txt', 'exe', 'dll']:
        return "File's name after dot should be one of: txt, exe, dll"
    
    return "Yes"