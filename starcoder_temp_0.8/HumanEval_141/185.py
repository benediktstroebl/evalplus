
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
    n = 0
    for char in file_name:
        if char.isnumeric():
            n += 1
        elif char == '.':
            if file_name.count('.') == 1 and file_name.index('.') == 0:
                return 'No'
            dot_index = file_name.index('.')
            substring_before_dot = file_name[:dot_index]
            substring_after_dot = file_name[dot_index+1:]
            if not substring_before_dot.isalpha():
                return 'No'
            if substring_after_dot not in ['txt', 'exe', 'dll']:
                return 'No'
            else:
                return 'Yes'
    if n > 3:
        return 'No'
    return 'Yes'

