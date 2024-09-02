
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

    # check if there is only 1 dot
    if '.' in file_name:
        if file_name.count('.') == 1:
            # if there is a dot split the string to before dot and after dot
            before_dot, after_dot = file_name.split('.')
            # check for validity
            if after_dot in ['txt', 'exe', 'dll'] and before_dot.replace(' ', '').isalpha():
                if before_dot[0].isalpha():
                    return 'Yes'
            elif before_dot.count('.') == 0:
                if before_dot[0].isalpha():
                    if before_dot.replace(' ', '').isalpha():
                        return 'Yes'
    return 'No'
