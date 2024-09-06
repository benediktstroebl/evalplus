
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
    def file_name_check_string(filename):
        if len(re.findall('[0-9]',filename)) > 3:
            return 'No'
        elif re.search('[.]',filename) == None:
            return 'No'
        else:
            tokens = filename.split('.')
            if len(tokens[0])>0 and tokens[0][0].isalpha():
                if len(tokens[1])!= 0 and tokens[1] in filetype:
                    return 'Yes'
                else:
                    return 'No'
            else:
                return 'No'
    return file_name_check_string(file_name)
