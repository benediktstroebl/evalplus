
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
    c_ok = False
    l_ok = False
    dot_ok = False
    dot_pos = 0
    pos = 0
    while pos < len(file_name):
        if file_name[pos].isdigit():
            c_ok = True
            if c_ok == True and file_name[pos + 1].isdigit() == True:
                c_ok = False
        if file_name[pos].isalpha():
            l_ok = True
        if file_name[pos] == '.':
            dot_ok = True
            dot_pos = pos
        pos += 1
    if not c_ok:
        if l_ok and dot_ok:
            if dot_pos != 0:
                if dot_pos + 1 < len(file_name):
                    if file_name[dot_pos + 1:] == 'txt':
                        print('Yes')
                    elif file_name[dot_pos + 1:] == 'exe':
                        print('Yes')
                    elif file
