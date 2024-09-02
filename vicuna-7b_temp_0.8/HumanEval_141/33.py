
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
    # Check if the file name is empty
    if len(file_name) == 0:
        return "No"
    
    # Check if there are more than three digits in the file name
    if re.search(r'\d+', file_name):
        return "No"
    
    # Check if the file name contains exactly one dot
    if re.search(r'\.', file_name) == None:
        return "No"
    
    # Check if the substring before the dot is empty or starts with a latin alphabet letter
    if re.search(r'^[a-z]', file_name[:len(file_name) - len(file_name.split('.')[0])]) == None:
        return "No"
    
    # Check if the substring after the dot is one of ['txt', 'exe', 'dll']
    if re.search(r'[\w\-]+\.[\w\-]+', file_name.split('.')[1]) == None:
        return "No"
    
    return "Yes"
