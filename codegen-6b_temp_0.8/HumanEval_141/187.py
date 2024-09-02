
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
    # pass
    # Hint: you can use .lower() and .replace()

    # If the file name contains more than 3 digits, return 'No'
    if re.findall("\d+",file_name):
        return 'No'
    # If the file name contains more than one dot, return 'No'
    if re.findall("\.", file_name):
        return 'No'
    # If the file name does not contain space, return 'No'
    if not re.findall(" ", file_name):
        return 'No'
    # If the file name does not start with a lowercase letter, return 'No'
    if not re.findall("[a-z]", file_name):
        return 'No'
    # If the file's name does not have a double extension, return 'No'
    if '.' not in file_name:
        return 'No'
    # If the file has a double extension, check that the double extension is equal to 'exe' or 'dll'
    double_ext = file_name.split(".")[1]
    if double_ext not in ['exe','dll']:
        return 'No'
    return 'Yes'



