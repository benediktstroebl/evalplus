
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
    # Your code here
    # Checks if there is more than 3 numbers
    if file_name.count("0123456789") > 3:
        return "No"
    # Checks if the name contains a dot
    if "." not in file_name:
        return "No"
    # Checks if the name starts with a letter
    if file_name[0].isalpha() != True:
        return "No"
    # Checks if the name contains a dot
    if "." not in file_name:
        return "No"
    # Checks if there is a substring after the dot
    if len(file_name.split(".")[1]) == 0:
        return "No"
    # Checks if the substring after the dot is valid
    if file_name.split(".")[1] not in ["txt", "exe", "dll"]:
        return "No"
    # If the file name is valid
    return "Yes"
