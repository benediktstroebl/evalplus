
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
    def check_filename():
        # case 1: no digits in string
        if not any(char.isdigit() for char in file_name):
            return 'Yes'
        # case 2: more than 3 digits
        elif not len(file_name) == 5:
            return 'No'
        # case 3: dot
        elif file_name.count('.') != 1:
            return 'No'
        # case 4: one dot is before the file name
        elif file_name.find('.') < file_name.find(file_name[:1]):
            return 'No'
        # case 5: three chars after the dot
        elif not (file_name[file_name.find('.')+1:] == 'txt' \
                  or file_name[file_name.find('.')+1:] == 'exe' \
                  or file_name[file_name.find('.')+1:] == 'dll'):
            return 'No'
        else:
            return 'Yes'
    return check_filename

