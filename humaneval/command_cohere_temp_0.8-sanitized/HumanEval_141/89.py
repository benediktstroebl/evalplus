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
    
    if len(file_name) > 10: 
        return "File name should not contain more than ten characters"
    
    dot_index = file_name.index('.') 
    if dot_index < 0 or len(file_name) - dot_index - 1 != 1: 
        return "File name should contain exactly one dot"
    
    prefix = file_name[:dot_index]
    if not prefix.isalpha() or not prefix.islower():
        return "File name prefix should be a letter, in lowercase"
    
    ext = file_name[dot_index+1:]
    allowed_ext = ['txt', 'exe', 'dll']
    if ext not in allowed_ext:
        return "File name extension should be amongst ['txt', 'exe', 'dll']"
    
    if len(set(file_name)) != len(file_name):
        return "File name should not contain more than three digits ('0'-'9')"
    
    return "Yes"