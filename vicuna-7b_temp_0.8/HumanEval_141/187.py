
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
    invalid_file_name = False
    invalid_prefix = False
    invalid_suffix = False
    invalid_middle = False

    if len(file_name) > 3:
        invalid_file_name = True
    if file_name.find(".") < 0:
        invalid_file_name = True
    if not file_name.startswith(chr(ord("a") + 0)):
        invalid_prefix = True
    if not re.match(r"\w+(\.\w+)*$", file_name[:len(file_name)-len(file_name.split(".")[-1])]):
        invalid_middle = True
    if file_name.split(".")[-1].lower() != "txt" and file_name.split(".")[-1].lower() != "exe" and file_name.split(".")[-1].lower() != "dll":
        invalid_suffix = True

    if invalid_file_name or invalid_prefix or invalid_suffix or invalid_middle:
        return "No"
    return "Yes"
