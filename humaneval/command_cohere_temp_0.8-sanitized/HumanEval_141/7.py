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
    
    if len(file_name) <= 1:
        return "File name should be more than one character"
    
    dot_index = file_name.find(".")
    if dot_index == -1 or dot_index == 0 or dot_index == len(file_name) - 1:
        return "File name should contain exactly one dot"
    
    prefix = file_name[:dot_index]
    if not prefix.startswith(tuple('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        return "The prefix of file name should start with a letter"
    
    if len(prefix) == 0:
        return "The prefix of file name should not be empty"
    
    if len(prefix) > 3 and prefix.isdigit():
        return "The prefix of file name should not have more than three digits"
    
    suffix = file_name[dot_index+1:]
    valid_suffix = ["txt", "exe", "dll"]
    if suffix not in valid_suffix:
        return "The suffix of file name should be one of: txt, exe, dll"
    
    return "Yes"