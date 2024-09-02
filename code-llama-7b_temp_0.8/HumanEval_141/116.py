
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
    # check that the name is not too long
    digits_count = len([x for x in file_name if x.isdigit()])
    if digits_count > 3:
        return 'No'
    # check that there is one dot in the name
    dot_count = 0
    for i in file_name:
        if i == '.':
            dot_count += 1
    if dot_count != 1:
        return 'No'
    # check that there is a letter before the dot
    before_dot = ''
    for i in file_name:
        if i != '.':
            before_dot += i
        else:
            break
    if before_dot.isdigit() or before_dot == '':
        return 'No'
    # check that the after dot is one of these: ['txt', 'exe', 'dll']
    after_dot = file_name.split('.')[-1]
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    # if all checks are passed, return yes
    return 'Yes'
