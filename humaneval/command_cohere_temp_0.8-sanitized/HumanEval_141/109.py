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
    
    if not file_name.isalpha():
        return "FileName must start with a letter"
    
    dot_index = file_name.rfind('.')
    if dot_index < 0:
        return "The file's name should contain exactly one dot '.'"
    if len(file_name) - dot_index - 1 > 3:
        return "There should not be more than three digits ('0'-'9') in the file's name."
    
    pre_dot = file_name[:dot_index]
    if not pre_dot.isalpha():
        return "File name should start with a letter"
    
    post_dot = file_name[dot_index+1:]
    if post_dot not in ['txt', 'exe', 'dll']:
        return "Files may only end with 'txt', 'exe' or 'dll'"
    
    return "Yes"