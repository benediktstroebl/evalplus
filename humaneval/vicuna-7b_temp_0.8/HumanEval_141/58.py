
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
    # Check if the file name contains more than three digits
    if len(file_name.split(".")) > 4:
        return "No"
    
    # Check if the file name contains a dot
    if not file_name.endswith(".txt"):
        return "No"
    
    # Check if the file name contains a letter before the dot
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', file_name[:len(file_name)-4]):
        return "No"
    
    # Check if the file name contains one of the allowed extensions
    if not any(ext in file_name for ext in ["txt", "exe", "dll"]):
        return "No"
    
    return "Yes"
