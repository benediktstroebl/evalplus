
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

    pattern_dot = '[A-Za-z]+\.[A-Za-z]+' # pattern for dots
    pattern_three_digits = '[0-9]{3}' # pattern for three digits
    
    if file_name == '':
        return 'Yes'
    elif file_name.count('.')!= 1:
        return 'No'
    elif len(file_name.replace('.','',1).strip()) == 0:
        return 'Yes'
    elif not file_name.replace('.','',1).strip().isalpha() or not file_name.split('.')[1] in ['exe', 'dll']:
        return 'No'
    elif file_name.replace('.','',1).strip()[0].isnumeric():
        return 'No'
    elif re.match(pattern_three_digits, file_name.replace('.','',1).strip()[-3:]) and file_name.split('.')[1] in ['exe', 'dll']:
        return 'Yes'
    elif re
