
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
    # check length of substring before dot
    substring_before_dot = file_name.split('.')[0]
    if len(substring_before_dot) == 0:
        return 'No'
    # check that the first symbol of substring before dot is latin alphapet
    if not 64 < ord(substring_before_dot[0]) < 91 and not 96 < ord(substring_before_dot[0]) < 123:
        return 'No'
    # check length of substring after dot
    substring_after_dot = file_name.split('.')[1]
    if len(substring_after_dot) == 0:
        return 'No'
    # check if substring after dot is txt, exe or dll
    if substring_after_dot != 'txt' and substring_after_dot != 'exe' and substring_after_dot != 'dll':
        return 'No'
    # check if the number of digits in file name is 3 or less
    if len([x for x in file_name if x.isdigit()]) > 3:
        return 'No'
    # if all checks pass, return 'Yes'
    return 'Yes'

