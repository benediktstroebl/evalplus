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
    if not file_name or not isinstance(file_name, str):
        return "Yes" 
    valid, n, name = True, 0, file_name
       
    # Checks for the number of digits in the file name
    if file_name.isdigit():
        n = file_name.replace('.','',1).find('.')
        name = file_name.replace('.','',1)
        if n > 3:
            valid = False    
            
    # Checks for the presence of exactly one dot in the file name
    if ".." in file_name or "." in file_name.replace("."):
        valid = False
    
    # Checks for the mandatory conditions for the substring before the dot
    if not name.isalpha():
        valid = False
    
    # Checks for the mandatory conditions for the substring after the dot    
    if not name.endswith('.txt') and not name.endswith('.exe') and not name.endswith('.dll'):
        valid = False
    
    if valid:
        return "Yes" 
    else:
        return "No"