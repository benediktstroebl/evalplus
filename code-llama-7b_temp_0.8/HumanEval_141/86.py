
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
    # Split the file name into two parts by the dot '.'
    parts = file_name.split(".")
    if len(parts) != 2:
        return "No"

    # Check if the name before the dot starts with a letter
    if len(parts[0]) == 0:
        return "No"
    elif not parts[0][0].isalpha():
        return "No"

    # Check if the name after the dot is one of the three file extensions
    if parts[1] not in ["txt", "exe", "dll"]:
        return "No"

    # Check if the name has more than three digits
    for character in parts[0]:
        if character.isdigit() and len(parts[0]) >= 4:
            return "No"
    
    return "Yes"
