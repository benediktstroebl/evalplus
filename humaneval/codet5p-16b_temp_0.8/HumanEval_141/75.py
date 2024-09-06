
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

    for digit in file_name:
        if digit.isdigit():
            return 'No'
    
    dot_position = file_name.find('.')
    if dot_position == -1:
        return 'No'
    
    substring_before_dot = file_name[:dot_position]
    if len(substring_before_dot) == 0:
        return 'No'
    
    if substring_before_dot[0].isalpha():
        return 'Yes'
    else:
        return 'No'
    
    substring_after_dot = file_name[dot_position+1:]
    if substring_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
