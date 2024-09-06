
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
    if len(file_name) < 4:
        return 'No'
    if len(file_name) > 4:
        return 'No'
    if file_name.count(".") > 1:
        return 'No'
    if file_name.count(".") < 1:
        return 'No'
    if file_name.count(".") == 1:
        if file_name.index('.') == 3:
            return 'No'
        if file_name.index('.') != 3:
            return 'Yes'
    if file_name.count(".") == 1:
        if len(file_name[0]) == 0:
            return 'No'
    if len(file_name) == 4:
        if file_name[0] != '.':
            return 'Yes'
        else:
            return 'No'
    if len(file_name) == 3:
        if file_name[0] != '.':
            return 'Yes'
        else:
            return 'No'
    if file_name[0].isalpha() is True:
        return 'Yes'
    if file_name[0].isalpha() is False:
        return 'No'
    if file_name[1].isdigit() is True:
        return 'No'
    if file_name[1].isdigit() is False:
        return 'Yes'
    if file_name[2].isdigit() is True:
        return 'No'
    if file_name[2].isdigit() is False:
        return 'Yes'
    if file_name[-3:].lower() == 'txt':
        return 'Yes'
    if file_name[-3:].lower() == 'exe':
        return 'Yes'
    if file_name[-3:].lower() == 'dll':
        return 'Yes'
    else:
        return 'No'
