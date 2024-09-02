
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
    # Check if file name has more than three digits
    if len(file_name) > 3:
        return "No"
    
    # Check if file name contains exactly one dot
    if not file_name.endswith(".") or file_name.endswith("."):
        return "No"
    
    # Check if the substring before the dot is empty or starts with a letter from the latin alphabet
    before_dot = file_name[:-2]
    if not before_dot or not re.match(r"^[a-zA-Z][a-zA-Z0-9]*$", before_dot):
        return "No"
    
    # Check if the substring after the dot is one of 'txt', 'exe', or 'dll'
    after_dot = file_name[:-2]
    if not after_dot in ['txt', 'exe', 'dll']:
        return "No"
    
    return "Yes"
