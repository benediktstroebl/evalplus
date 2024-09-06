
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
    # check for digit in file_name
    if '0' <= file_name[0] <= '9':
        return 'No'
    # check for dot in file_name
    dot = file_name.find('.')
    if dot == -1 or file_name.find('.', 0, dot) == dot:
        return 'No'
    # check for empty substring before dot
    if file_name[1:].strip() == '':
        return 'No'
    # check for valid extension
    ext = file_name.split('.')[1].lower()
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
