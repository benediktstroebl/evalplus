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
        return "No"
    alphanumeric_count = sum(char.isdigit() or char.isalpha() for char in file_name)
    if alphanumeric_count > 3:
        return "No"
    dot_position = file_name.find(".")
    if dot_position == -1 or dot_position == 0 or dot_position == len(file_name) - 1:
        return "No"
    prefix = file_name[:dot_position]
    if not prefix.startswith(tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")):
        return "No"
    postfix = file_name[dot_position+1:]
    valid_postfix = postfix in ["txt", "exe", "dll"]
    if not valid_postfix:
        return "No"
    return "Yes"