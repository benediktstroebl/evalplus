
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
    try:
        if re.match(r"^[\w.]{0,3}\.txt$", file_name) is not None or \
            re.match(r"^[\w.]{0,3}\.exe$", file_name) is not None or \
                re.match(r"^[\w.]{0,3}\.dll$", file_name) is not None:
            return 'Yes'
        return 'No'
    except re.error:
        return 'No'
