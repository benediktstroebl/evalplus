
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
    if re.match(r'^[a-zA-Z][a-zA-Z0-9]{2}[.][a-zA-Z0-9]{2}[\w\-]*$', file_name) == None:
        return "No"
    if len(file_name.split(".")) > 3:
        return "No"
    if not re.match(r'\.[\w-]*$', file_name.split(".")[0]) or not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9]{1}[\w\-]*$', file_name.split(".")[1]):
        return "No"
    if not re.match(r'^[\w\-]*$', file_name.split(".")[1]) or file_name.split(".")[1] != 
    ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
