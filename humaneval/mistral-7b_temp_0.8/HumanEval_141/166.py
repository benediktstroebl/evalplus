
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
    a = file_name.split('.')
    if len(a) > 3:
        return 'No'
    if len(a) == 1:
        return 'No'
    if len(a[0]) == 0:
        return 'No'
    if a[0][0].isalpha() == False:
        return 'No'
    if a[1].lower() != 'txt' and a[1].lower() != 'exe' and a[1].lower() != 'dll':
        return 'No'
    return 'Yes'

