
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
    file_name_list = file_name.split('.')

    if len(file_name_list) != 2:
        return 'No'
    
    _, ext = file_name_list
    
    tag_list = ['txt', 'exe', 'dll']
    
    return 'Yes' if ext in tag_list and file_name_list[0].lower() and file_name_list[0][0].lower() in 'abcdefghijklmnopqrstuvwxyz' and file_name_list[1][0].lower() in 'abcdefghijklmnopqrstuvwxyz0123456789' else 'No'
