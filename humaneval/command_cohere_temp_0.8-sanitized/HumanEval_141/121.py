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

    # Check if the file name contains more than 3 digits
    if re.search(r'\d{4,}', file_name):
        return "No"
    
    # Check for exactly one dot '.' in the file name
    if ".".join(file_name.split(".")[-2:]) == file_name:
        return "No"
    
    # Check for valid substrings after the dot
    if not file_name.split(".")[1]:
        return "No"

    file_extension = file_name.split(".")[1]
    if file_extension not in ['txt', 'exe', 'dll']:
        return "No"
    
    # Check for a letter as the first character in the file name before the dot
    if not file_name.split(".")[0][0].isalpha():
        return "No"
    
    return "Yes"