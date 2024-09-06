
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
    if len(file_name) > 2:
        raise ValueError('The file name should have no more than three digits.')
    dot_index = file_name.find('.')
    if dot_index < 0:
        raise ValueError('The file name should contain exactly one dot.')
    if not file_name[0].isalpha():
        raise ValueError('The file name should start with a latin alphapet letter.')
    file_extension = file_name[dot_index+1:]
    if file_extension not in ['txt', 'exe', 'dll']:
        raise ValueError('The file extension should be one of [txt, exe, dll].')
    return 'Yes'


    file_name_check(file_name)
    print(ex)
    print(f'Yes, the file name is valid: {file_name}')
