
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
    # Check for more than 3 digits in the file name
    if re.match(r'\d{4}', file_name):
        return 'No'

    # Check for the dot
    if re.search(r'\.', file_name) is None:
        return 'No'

    # Check for the letters
    prefix = file_name[:3]
    if not re.match(r'^[a-zA-Z]+$', prefix):
        return 'No'

    suffix = file_name[3:]
    suffix_allowed = ['txt', 'exe', 'dll']
    if suffix not in suffix_allowed:
        return 'No'

    return 'Yes'
