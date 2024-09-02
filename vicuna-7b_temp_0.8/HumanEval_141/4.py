
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
    # check if the file name contains more than 3 digits
    if re.search(r'\d{4}', file_name):
        return "No"
    
    # check if the file name contains a dot
    if "." not in file_name:
        return "No"
    
    # check if the substring before the dot is empty or starts with a letter
    if len(file_name.split(".")[0]) == 0 or not re.match(r'^[a-zA-Z]+', file_name.split(".")[0]):
        return "No"
    
    # check if the substring after the dot is one of the expected extensions
    extensions = ["txt", "exe", "dll"]
    if not any(ext in file_name.split(".")[1] for ext in extensions):
        return "No"
    
    return "Yes"
