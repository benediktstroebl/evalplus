
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
    file_name = str(file_name)
    if '.' in file_name:
        start_of_file, end_of_file = file_name.split('.')
        if len(start_of_file) > 0:
            if len(start_of_file) <= 3:
                if start_of_file[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or len(start_of_file) == 0:
                    if end_of_file == 'txt' or end_of_file == 'dll' or end_of_file == 'exe':
                        return 'Yes'
    return 'No'

