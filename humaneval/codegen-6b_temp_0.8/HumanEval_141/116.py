
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
    import string
    def is_valid_file_name(file_name):
        # count the digits
        digit = -1
        for c in file_name:
            if c in string.digits:
                digit += 1
        if digit > 1: # more than one digit
            return 'No'
        elif digit == 1: # one digit
            if file_name[0] not in string.ascii_letters: # the first character is not a latin alphapet
                return 'No'
            else:
                dot = file_name.find('.')
                if dot == -1: # no dot
                    return 'No'
                else: # with a dot
                    if dot == 0: # the dot is at the beginning
                        return 'No'
                    # check the substring after the dot
                    for extension in ['txt', 'exe', 'dll']:
                        if file_name[dot+1:] == extension:
                            return 'Yes'
    return is_valid_file_name(file_name)





