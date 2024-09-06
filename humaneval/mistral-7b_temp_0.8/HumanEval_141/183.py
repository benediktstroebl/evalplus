
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
    substring_before_dot = ''
    substring_after_dot = ''
    is_valid = True
    if file_name.endswith('.txt') or file_name.endswith('.dll') or file_name.endswith('.exe'):
        is_valid = True
    else:
        is_valid = False
    if is_valid:
        if file_name.count('.') > 1:
            is_valid = False
        if file_name.count('.') == 0:
            is_valid = False
        if file_name.endswith('.txt') or file_name.endswith('.dll') or file_name.endswith('.exe'):
            is_valid = True
        if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6
