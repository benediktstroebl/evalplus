
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
    # first check for digits
    digits = 0
    for char in file_name:
        if char.isdigit():
            digits += 1
    if digits > 3:
        return "No"

    # then check for dots
    dots = file_name.count(".")
    if dots != 1:
        return "No"

    # check substring after dot
    after_dot = file_name.split(".")[1]
    if after_dot.lower() not in ["txt", "exe", "dll"]:
        return "No"

    # finally check substring before dot
    before_dot = file_name.split(".")[0]
    if not before_dot.isalpha():
        return "No"
    return "Yes"

