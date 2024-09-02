
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
    error_msg = """File name must be a string"""
    if not isinstance(file_name, str):
        raise TypeError(error_msg)
    elif file_name == "":
        raise ValueError("""File name can't be an empty string""")
    elif file_name[0] in string.ascii_letters and file_name[0].isalpha():
        name = file_name.split(". ")
        if len(name) == 2:
            if name[1] == "dll" or name[1] == "exe" or name[1] == "txt":
                return "Yes"
            else:
                raise ValueError("""File name should contain only letters, a dot, and one of the following: ['exe', 'dll', 'txt']""")
        else:
            raise ValueError("""File name must contain two words""")
    else:
        raise ValueError("""File name must start with a letter""")
