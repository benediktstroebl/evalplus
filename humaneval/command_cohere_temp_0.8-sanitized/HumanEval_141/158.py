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
    if not file_name or not isinstance(file_name, str):
        return "No"
    invalid = False
    # Check for more than three consecutive digits in the file name
    if ('0' <= file_name[i:] <= '9' for i in range(len(file_name))).count(True) > 3:
        return "No"
    # Check for exactly one dot in the file name
    if sum(file_name.count('.') for file_name in [file_name, file_name.swapcase()]) != 1:
        return "No"
    # Check for valid file extension and prefix
    if not file_name.count('.') and not (file_name[0].isalpha() and file_name[1:].replace('_', 'a')):
        return "No"
    ext = file_name.split('.')[-1].lower()
    if ext not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"