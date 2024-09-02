
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
    #Find out if the file name has 3 digits
    num_count = 0
    for char in file_name:
        if char.isdigit():
            num_count += 1
    if num_count > 3:
        return "No"
    #Find out if the file name has one dot
    dot_count = 0
    for char in file_name:
        if char == ".":
            dot_count += 1
    if dot_count != 1:
        return "No"
    #Find out if the substring before the dot is a letter
    for char in file_name[:file_name.index(".")]:
        if char.isalpha():
            continue
        else:
            return "No"
    #Find out if the substring after the dot is a valid extension
    if file_name[file_name.index("."):] not in [".txt", ".exe", ".dll"]:
        return "No"
    #If all the conditions are met, then return "Yes"
    return "Yes"
