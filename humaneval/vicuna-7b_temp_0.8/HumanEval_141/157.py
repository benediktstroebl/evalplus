
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
    # check for digits
    if len(file_name) >= 4:
        return "No"
    
    # check for dot
    dot = file_name.find('.')
    if dot == -1:
        return "No"
    
    # check for letters before dot
    before_dot = file_name[:dot]
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', before_dot):
        return "No"
    
    # check for allowed extensions
    extensions = ["txt", "exe", "dll"]
    if not extensions.count(file_name[dot+1:].lower()) != 1:
        return "No"
    
    return "Yes"
