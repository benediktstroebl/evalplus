
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
    # checking if there are less than 3 digits in file_name
    digits_count = 0
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    
    # checking if there are exactly 1 dot in file_name
    dot_count = 0
    for i in range(len(file_name)):
        if file_name[i] == '.':
            dot_count += 1
    if dot_count != 1:
        return 'No'
    
    # checking if there is no empty substring before the dot
    for i in range(len(file_name)):
        if file_name[i] == '.':
            if len(file_name[:i]) == 0:
                return 'No'
            else:
                break
    
    # checking if the substring before the dot starts with a latin alphabet letter
    if file_name[:i][0].isalpha() == False:
        return 'No'
    
    # checking if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if file_name[i+1:] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # all checks were successful
    return 'Yes'
