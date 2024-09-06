
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
    digits_count = 0
    if "." in file_name:
        splitted = file_name.split(".")
        if len(splitted[0]) == 0:
            return "No"
        if len(splitted) > 2:
            return "No"
        if splitted[1] not in ["txt", "exe", "dll"]:
            return "No"
        for char in splitted[0]:
            if char in "0123456789":
                digits_count += 1
            if digits_count > 3:
                return "No"
        return "Yes"
    return "No"

