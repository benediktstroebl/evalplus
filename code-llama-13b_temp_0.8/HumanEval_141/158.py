
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
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters += letters.upper()
    split_name = file_name.split(".")
    if len(split_name) > 2:
        return "No"
    if len(split_name) == 1:
        return "No"
    if len(split_name[1]) == 0:
        return "No"
    if len(split_name[0]) == 0:
        return "No"
    if file_name.find(".") == 0:
        return "No"
    if len(split_name) == 2:
        if (split_name[0][0] not in letters) or (split_name[1] not in ["txt", "exe", "dll"]):
            return "No"
    if split_name[0].isdigit() or split_name[1].isdigit():
        return "No"
    for letter in split_name[0] + split_name[1]:
        if letter in "0123456789":
            return "No"
    return "Yes"
    
