
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
    try:
        substring_before_dot = file_name[:file_name.index(".")]
        substring_after_dot = file_name[file_name.index("."):]
        is_valid = True
    except:
        is_valid = False
        return "No"
    if not substring_before_dot[0].isalpha():
        is_valid = False
        return "No"
    if substring_after_dot not in [".txt", ".exe", ".dll"]:
        is_valid = False
        return "No"
    if len([i for i in file_name if i.isdigit()]) > 3:
        is_valid = False
        return "No"
    if is_valid:
        return "Yes"
    return "No"
