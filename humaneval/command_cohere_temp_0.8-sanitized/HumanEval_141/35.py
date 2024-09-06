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
    
    if len(file_name) <= 1:
        return "File's name should be more than one character"
    
    dot_index = file_name.rfind('.')
    if dot_index <= 0 or dot_index == len(file_name) - 1:
        return "File's name should contain exactly one dot"
    
    prefix = file_name[:dot_index]
    suffix = file_name[dot_index+1:]
    
    if prefix.strip().lower().startswith('www.') or prefix.strip().lower().startswith('http.') or prefix.strip().lower().startswith('www'):
        return "File's name should not start with 'www' or 'http'"
    
    if suffix not in ['txt', 'exe', 'dll']:
        return "File's name extension should be 'txt', 'exe' or 'dll'"
    
    if prefix.isdigit():
        return "File's name prefix should not consist of more than three digits"
    
    return "Yes"