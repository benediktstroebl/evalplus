
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

    list_numbers = ['0','1','2','3','4','5','6','7','8','9']
    if len(file_name) > 3:
        return 'No'
    for number in list_numbers:
        if number in file_name:
            return 'No'
    if '.' not in file_name:
        return 'No'
    list_dot = file_name.split('.')
    if len(list_dot) > 2:
        return 'No'
    substring_before_dot = list_dot[0]
    if not len(substring_before_dot):
        return 'No'
    if not substring_before_dot[0].isalpha():
        return 'No'
    substring_after_dot = list_dot[1]
    if substring_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
