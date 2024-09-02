
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
    # Check the length of the file's name
    if len(file_name) > 3:
        return "No"
    
    # Check if the file's name contains exactly one dot
    if not file_name.endswith(".") or len(file_name) == 1:
        return "No"
    
    # Check the substring before the dot
    before_dot = file_name[:3]
    if not any(c.isalpha() for c in before_dot):
        return "No"
    
    # Check the substring after the dot
    if not any(file_name[3:] in ["txt", "exe", "dll"]) and file_name[3:] not in ["", "txt", "exe", "dll"]:
        return "No"
    
    return "Yes"
