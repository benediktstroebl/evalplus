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
        return "File name should be rather short"
    
    dot_index = file_name.find(".")
    if dot_index == -1: 
        return "File should contain exactly one dot"
    substring_before_dot = file_name[:dot_index]
    substring_after_dot = file_name[dot_index+1:]
    
    if len(substring_after_dot)-len(set(substring_after_dot.split())) > 1 or \
            substring_after_dot not in ['txt', 'exe', 'dll']:
        return "File extension should be unique and one of predefined"
    
    if substring_before_dot == "":
        return "File name should not be empty"
    
    if not substring_before_dot[0].isalpha():
        return "File name should start with a letter"
    
    if len(substring_before_dot)-len(set(substring_before_dot.split())) > 3:
        return "There should not be more than three digits in the file's name"
    
    return "Yes"