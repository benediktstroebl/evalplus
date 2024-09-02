
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
    # Check if the file name has more than 3 digits
    if len(file_name) > 3:
        return "No"
    
    # Check if the file name contains exactly one dot
    if file_name.count(".") != 1:
        return "No"
    
    # Check if the string before the dot is empty or starts with a letter from the latin alphabet ('a'-'z' or 'A'-'Z')
    if file_name[:1].lower() == "" or file_name[:1] not in "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "No"
    
    # Check if the substring after the dot is one of the allowed extensions
    allowed_extensions = ["txt", "exe", "dll"]
    if not any(file_name.count(extension) > 0 for extension in allowed_extensions):
        return "No"
    
    return "Yes"
