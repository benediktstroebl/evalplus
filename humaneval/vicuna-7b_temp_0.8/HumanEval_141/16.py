
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
    # First check for more than 3 digits in the file's name
    if re.search(r'\d{4,}', file_name):
        return "No"

    # Then check if the file's name contains exactly one dot
    if re.search(r'\.[\w.]*', file_name) is None:
        return "No"

    # Then check if the substring before the dot starts with a letter
    if re.search(r'^[\w\s]*', re.search(r'\.[\w.]*', file_name).group(0)) is None:
        return "No"

    # Then check if the substring after the dot is one of the allowed extensions
    allowed_extensions = ['txt', 'exe', 'dll']
    for extension in allowed_extensions:
        if re.search(r'\.%s$' % extension, file_name):
            return "Yes"
    return "No"