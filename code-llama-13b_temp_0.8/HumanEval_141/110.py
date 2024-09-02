
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
    # your code here
    new_file_name = file_name.split(".")
    sub_file_name = new_file_name[0]
    sub_file_type = new_file_name[1]
    if len(file_name.split(".")) != 2:
        return "No"
    if len(new_file_name[0]) == 0 or new_file_name[0][0].isdigit() or new_file_name[0][0].isdigit():
        return "No"
    if not sub_file_name[0].isalpha():
        return "No"
    if sub_file_type != "txt" and sub_file_type != "exe" and sub_file_type != "dll":
        return "No"
    for char in sub_file_name:
        if not char.isalnum() and char != "." and char != "_":
            return "No"
    return "Yes"
