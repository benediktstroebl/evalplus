
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
    # Hint: You can check whether a substring is present in a string by using the built-in function
    # find(). You can check whether a substring starts with a latin alphabet letter by using the 
    # built-in function isalpha(). You can check the length of a string by using the built-in 
    # function len()
    if len(file_name) > 3:
        return "No"
    if file_name.find(".") == -1:
        return "No"
    if not file_name[:file_name.find(".")].isalpha():
        return "No"
    if file_name[-3:] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"

