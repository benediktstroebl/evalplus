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
    if not isinstance(file_name, str):
        return "File name should be a string"
    
    if len(file_name) == 0:
        return "File name should not be empty"
    
    elif file_name.find(".") != len(file_name) - 1:
        return "File should contain exactly one dot"
    
    else:
        before_dot, after_dot = file_name.split(".")
        
        if len(after_dot) != 3:
            return "The file extension should be exactly three characters"
        
        elif after_dot not in ["txt", "exe", "dll"]:
            return "File extension should be only: txt, exe or dll"
        
        elif before_dot.isalpha() and len(before_dot) > 0 and len(before_dot.replace(".", "").replace("0123456789", "")) <= 2:
            return "Yes"
        else:
            return "No"