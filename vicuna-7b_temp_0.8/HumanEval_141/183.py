
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
    # check length of the file name
    if len(file_name) > 3:
        return "No"
    
    # check if file name contains a dot
    if file_name.find(".") == -1:
        return "No"
    
    # check if the substring before the dot is empty or starts with a non-latin alphabet
    if file_name[:1].isdigit() or file_name[:1] != letter:
        return "No"
    
    # check if the substring after the dot is one of the allowed file types
    if file_name[file_name.rfind(".")+1:] not in ["txt", "exe", "dll"]:
        return "No"
    
    return "Yes"
