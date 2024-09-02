
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
    is_valid = True

    # check if there are more than 3 digits in the file's name
    for i in range(10):
        if str(i) * 4 in file_name:
            is_valid = False
            break
    # check for the dot
    if not ("." in file_name):
        is_valid = False
    # check for the valid characters before the dot
    if not file_name[0].isalpha():
        is_valid = False
    # check for the valid characters after the dot
    if file_name.split(".")[-1] not in ["txt", "exe", "dll"]:
        is_valid = False

    return "Yes" if is_valid else "No"

