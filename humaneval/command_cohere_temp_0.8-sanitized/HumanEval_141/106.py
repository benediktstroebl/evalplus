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

    # Check if the file name contains a dot exactly once
    if '.' not in file_name:
        return 'No'

    # Check if the file name before the dot conforms to the rules
    before_dot = file_name.split('.')[0]
    if not before_dot:
        return 'No'
    if not (before_dot[0].isalpha() and len(before_dot) <= 1):
        return 'No'

    # Check if the file name after the dot is in the list
    extensions = file_name.split('.')[1:]
    if not extensions or extensions[0] not in ['txt', 'exe', 'dll']:
        return 'No'

    # Check if there are not more than three digits in the file name
    if len(filter(str.isdigit, file_name)) > 3:
        return 'No'

    return 'Yes'