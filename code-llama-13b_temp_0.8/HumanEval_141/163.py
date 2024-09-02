
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
    check = False
    dot = False
    alpha = False
    substring1 = file_name[0:file_name.find('.')]
    substring2 = file_name[file_name.find('.') + 1:]
    if len(substring1) == 0:
        check = False
    else:
        for i in range(len(substring1)):
            if 48 <= ord(substring1[i]) <= 57:
                check = True
    if file_name.count('.') == 1:
        dot = True
    if 97 <= ord(substring1[0]) <= 122 or 65 <= ord(substring1[0]) <= 90:
        alpha = True
    if substring2 in ['txt', 'exe', 'dll']:
        check_list = [check, dot, alpha]
        if False in check_list:
            return 'No'
        else:
            return 'Yes'
    else:
        return 'No'

