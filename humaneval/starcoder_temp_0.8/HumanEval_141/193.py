
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
    is_valid = True
    max_number_of_digits = 3
    max_file_type_length = 3
    dot_index = file_name.find('.')
    file_type = file_name[dot_index+1:]
    digits_number = 0

    for char in file_name:
        if char.isdigit():
            digits_number += 1
    
    if digits_number > max_number_of_digits:
        is_valid = False

    if dot_index == 0 or dot_index == len(file_name) - 1:
        is_valid = False
    
    if not file_name[0].isalpha():
        is_valid = False
    
    if file_type.lower() not in ['txt', 'exe', 'dll']:
        is_valid = False
    
    return 'Yes' if is_valid else 'No'


