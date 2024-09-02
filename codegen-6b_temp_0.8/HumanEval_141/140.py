
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
    
    import re
    cond1 = re.sub(r'\D', '', file_name)
    cond2 = re.search(r'^[a-zA-Z][a-zA-Z]', cond1)
    cond3 = len(re.sub(r'\..*', '', file_name)) == 2
    cond4 = len(re.sub(r'\..*', '', file_name)) == 3
    cond5 = file_name.count('.') == 1
    if cond1 and cond2 and cond3 and cond4 and cond5:
        return 'Yes'
    return 'No'
