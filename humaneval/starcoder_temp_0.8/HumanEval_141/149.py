
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
    if '.' in file_name:
        name_before_dot, name_after_dot = file_name.split('.')
        if name_before_dot.isdigit():
            return "No"
        if name_after_dot not in ['txt', 'exe', 'dll']:
            return "No"
        if len(name_before_dot) == 0 or name_before_dot[0] not in string.ascii_letters:
            return "No"
    return "Yes"
