
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
    import re
    file_name = file_name.strip()
    result = False
    if len(file_name.split(".")) == 2:
        substrings = file_name.split(".")
        if substrings[0].isalpha() and substrings[1] in ["txt", "exe", "dll"]:
            result = True
    if re.match(r"^[a-zA-Z]", file_name):
        if re.match(r"^\d+$", file_name):
            return False
        if re.match(r"^[a-zA-Z]+[0-9]+$", file_name):
            return False
        if re.match(r"^[a-zA-Z].*\d$", file_name):
            return False
        if re.match(r"^[a-zA-Z].*[0-9].*[0-9]$", file_name):
            return False
    return result
    # return result
