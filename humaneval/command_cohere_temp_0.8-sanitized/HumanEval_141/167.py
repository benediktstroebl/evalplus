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
    if dot_index == -1:  # No dot found, the file name is invalid
        return "No"

    prefix = file_name[:dot_index]
    if len(prefix) == 0 or not prefix.isalpha():  # Invalid prefix
        return "No"

    suffixt = file_name[dot_index+1:]
    if len(suffixt) == 0 or suffixt != "txt" and suffixt != "exe" and suffixt != "dll":  # Invalid suffix
        return "No"

    num_counter = 0
    for char in file_name:
        if char.isdigit():
            num_counter += 1
    if num_counter > 3:  # More than three digits are not allowed
        return "No"
    
    return "Yes"