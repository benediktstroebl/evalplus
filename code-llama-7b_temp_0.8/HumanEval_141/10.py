
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

    # 1) check if there are less than or more than three digits in the file name
    if len([s for s in file_name if s.isdigit()]) > 3:
        return 'No'
    
    # 2) check if the file name contains more than one '.'
    elif file_name.count('.') != 1:
        return 'No'

    # 3) check if the file name starts with a latin alphapet letter
    elif len(file_name.split('.')[0]) == 0:
        return 'No'
    
    # 4) check if the file extension is one of the following: ['txt', 'exe', 'dll']
    elif file_name.split('.')[-1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    else:
        return 'Yes'

