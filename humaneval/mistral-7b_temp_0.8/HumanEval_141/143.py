
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
    # Write your code here
    # ~~~~~~~~~~~~~~~~~~~~~~~

    name_parts = file_name.split('.')

    if len(name_parts) != 2:
        return "No"

    if name_parts[0].isdigit():
        return "No"

    if len(name_parts[1]) > 3:
        return "No"

    if name_parts[1] not in ["txt", "dll", "exe"]:
        return "No"

    return "Yes"


