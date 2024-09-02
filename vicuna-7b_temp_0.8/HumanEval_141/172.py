
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
    # Check if there are more than 3 digits in the file name
    if sum([int(c) for c in file_name]) > 3:
        return 'No'

    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Check if the substring before the dot is empty, or starts with a latin alphabetic character
    if file_name.find('.') < 1 or not re.match('^[a-zA-Z][a-zA-Z0-9]*', file_name[:file_name.find('.')]):
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    extensions = ['txt', 'exe', 'dll']
    if not any(extensions.startswith(file_name[file_name.find('.')+1:]) for file_name in extensions):
        return 'No'

    return 'Yes'