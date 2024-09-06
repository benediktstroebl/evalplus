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
        return "File's name should be a string"
    
    if not file_name.isalpha():
        return "FileName must start with a letter"
    
    dot_index = file_name.find(".")
    if dot_index < 0 or dot_index + 1 == len(file_name):
        return "The file's name should contain exactly one dot"
    
    prefix = file_name[:dot_index]
    if not prefix.isalpha():
        return "File prefix should start with a letter"
    
    if prefix.count(".") > 1:
        return "More than one dot is not allowed"
    
    if dot_index + 2 == len(file_name):
        return "File suffix is missing"
    
    suffix = file_name[dot_index + 1:]
    allowed_suffix = ["txt", "exe", "dll"]
    if suffix not in allowed_suffix:
        return f"Invalid file suffix. Should be one of {', '.join(allowed_suffix)}"
    
    digits = prefix.count("0123456789")
    if digits > 3:
        return "More than three digits is not allowed in the prefix"
    
    return "Yes"