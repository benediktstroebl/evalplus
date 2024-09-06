
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

    digits = 0
    name_length = len(file_name)
    dot = file_name.rfind('.')
    if dot > 0 and dot < name_length - 3:
        substr = file_name[:dot]
        if substr:
            if substr[0].isalpha():
                substr_after_dot = file_name[dot + 1:]
                if substr_after_dot in ['txt', 'exe', 'dll']:
                    return 'Yes'
    return 'No'

