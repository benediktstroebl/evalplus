
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

    # split the filename and check if it has exactly one '.'
    filename = file_name.split('.')
    if len(filename) != 2:
        return 'No'

    # check if the first part of the filename is not empty
    if filename[0] == '':
        return 'No'

    # check if the first part of the filename starts with a letter
    if filename[0][0].isalpha() == False:
        return 'No'

    # check if the first part of the filename has more than three digits
    if len(filename[0]) > 3:
        return 'No'

    # check if the last part of the filename is one of these: ['txt', 'exe', 'dll']
    if filename[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
