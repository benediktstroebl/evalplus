
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
    count = 0
    file_name = file_name.split(".")
    if len(file_name) < 2:
        return "No"
    elif len(file_name) == 2:
        if len(file_name[0]) == 0:
            return "No"
        elif len(file_name[1]) == 0:
            return "No"
        elif len(file_name[0]) > 3:
            return "No"
        elif file_name[1] != "txt" and file_name[1] != "exe" and file_name[1] != "dll":
            return "No"
        else:
            return "Yes"
    else:
        return "No"


