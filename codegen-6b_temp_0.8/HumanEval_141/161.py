
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
    def check(string):
        if re.match(r'^[a-z]+', string) is None:
            return 'No'
        else:
            string = string.replace('.', '')
            if len(string) == 0:
                return 'No'
            elif re.match(r'^[a-zA-Z]', string[0]):
                return 'No'
            elif re.match(r'[0-9]', string[-1]):
                return 'No'
            elif re.match(r'[a-zA-Z]+', string[-1]):
                substring = string[-1]
                if len(string) > 2:
                    if substring == 'exe' or substring == 'dll':
                        return 'Yes'
                    else:
                        return 'No'
                else:
                    return 'No'
    return check(file_name)
