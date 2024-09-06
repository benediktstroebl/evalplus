
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
    # check if there are more than 3 digits in the file name
    if len(file_name) > 3:
        return "No"
    
    # check if the file name contains a dot
    if "." not in file_name:
        return "No"
    
    # check if the substring before the dot is empty or starts with a latin alphabet letter
    before_dot = file_name.split(".")[0]
    if before_dot == "" or not letter_in_alphabet(before_dot):
        return "No"
    
    # check if the substring after the dot is one of the valid extensions
    valid_extensions = ["txt", "exe", "dll"]
    if file_name.split(".")[1].lower() not in valid_extensions:
        return "No"
    
    return "Yes"
