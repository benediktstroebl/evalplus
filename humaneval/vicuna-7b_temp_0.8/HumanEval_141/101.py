
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
    # Regular expression to check if the file name is valid
    re_pattern = re.compile(r'\d+')
    re_pattern = re.compile(r'\.')
    re_pattern = re.compile(r'[a-zA-Z]')
    re_pattern = re.compile(r'\.([a-zA-Z]+)$')

    # If the file name is empty, return 'No'
    if not file_name:
        return "No"

    # Replace dots with empty string and remove all digits
    file_name = re.sub(r'\.', '', file_name)
    file_name = re.sub(r'\d+', '', file_name)

    # Split the file name by dot
    name, extension = file_name.split('.')

    # If the extension is not 'txt', 'exe' or 'dll', return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return "No"

    return "Yes"
