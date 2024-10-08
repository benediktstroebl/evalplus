
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
    # check that there are less than three digits in the file name
    if sum(map(str.isdigit, file_name)) > 3:
        return "No"
    
    # check for the existence of a dot and that the file name does not start with a dot
    if not '.' in file_name or file_name[0] == '.':
        return "No"
    
    # split file name into two parts: the substring before the first dot, and the substring after the dot
    file_name_split = file_name.split('.', 1)

    # check that the substring before the dot is not empty and that it starts with a latin alphapet letter
    if len(file_name_split[0]) == 0 or not (file_name_split[0][0].isalpha() or file_name_split[0][0].isupper()):
        return "No"

    # check that the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if not file_name_split[1] in ['txt', 'exe', 'dll']:
        return "No"
    
    return "Yes"
