
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
    if file_name.count('.') > 1: # only one dot
        return "No"
    else:
        dot = file_name.find('.')
        name = file_name[:dot]
        if name == "": # substring before the dot should not be empty
            return "No"
        elif not name[0].isalpha(): # the substring before the dot should start with a letter
            return "No"
        elif name[len(name) - 1].isdigit(): # there should not be more than three digits ('0'-'9') in the file's name
            return "No"
        else:
            suffix = file_name[dot + 1:]
            if suffix not in ["txt", "exe", "dll"]:
                return "No"
            else:
                return "Yes"
