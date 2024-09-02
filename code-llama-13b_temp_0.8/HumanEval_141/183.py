
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
    # Your code goes here
    is_name_valid = True
    if file_name.count('.') != 1:
        return 'No'
    if file_name[0].isalpha() == False:
        return 'No'
    if file_name[-4:] in ['txt', 'exe', 'dll'] == False:
        return 'No'
    for i in range(len(file_name)):
        if file_name[i].isdigit() and file_name[i] != '0' and file_name[i] != '1' and file_name[i] != '2' and file_name[i] != '3' and file_name[i] != '4' and file_name[i] != '5' and file_name[i] != '6' and file_name[i] != '7' and file_name[i] != '8' and file_name[i] != '9':
            is_name_valid = False
        if file_name[i] == '.' and file_name[i+1:].isdigit():
            is_name_valid = False
    if is_name_valid:
        return 'Yes'
    else:
        return 'No'
