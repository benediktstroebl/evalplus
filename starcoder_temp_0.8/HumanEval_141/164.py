
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
    # Your code here
    count_digits = 0
    for i in file_name:
        if i in '0123456789':
            count_digits += 1
            if count_digits > 3:
                return 'No'
    if file_name.count('.')!= 1:
        return 'No'
    else:
        index_dot = file_name.index('.')
        if index_dot == 0 or file_name[index_dot - 1] in '0123456789':
            return 'No'
        else:
            if file_name[index_dot+1:] not in ['txt', 'exe', 'dll']:
                return 'No'
            else:
                return 'Yes'
