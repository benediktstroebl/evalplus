
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
    i = 0
    for c in file_name:
        if i == 3:
            return 'No'
        if ord(c) >= 48 and ord(c) <= 57:
            i += 1
    
    if i >= 3:
        return 'No'
    
    if ord(file_name[0]) < 65 or (ord(file_name[0]) > 90 and ord(file_name[0]) < 97) or ord(file_name[0]) > 122:
        return 'No'

    ext = file_name[file_name.index('.') + 1 :]
    if ext != 'txt' and ext != 'exe' and ext != 'dll':
        return 'No'
    
    return 'Yes'
