
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
    name = str(file_name)
    name = name.replace(" ", "")
    if len(name) > 20:
        return "No"
    name_list = name.split(".")
    if len(name_list) > 3 or len(name_list) < 2:
        return "No"
    if name.isdigit():
        return "No"
    if name.isalpha():
        return "No"
    if len(name_list[0]) == 0:
        return "No"
    if name_list[1] == "txt" or name_list[1] == "exe" or name_list[1] == "dll":
        return "Yes"
    return "No"
