
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
    valid_file_type = ['txt', 'exe', 'dll']
    split_str = file_name.split(".")
    char_list = list(file_name)
    is_char_valid = False
    
    for char in char_list:
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            is_char_valid = True
            break
    
    if len(split_str) != 2 or split_str[0] == "" or is_char_valid == False:
        return "No"
    
    if split_str[1] in valid_file_type:
        if sum(c.isdigit() for c in file_name) <= 3:
            return "Yes"
        else:
            return "No"
    else:
        return "No"
