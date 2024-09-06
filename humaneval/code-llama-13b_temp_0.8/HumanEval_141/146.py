
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
    return_value = "No"

    if '.' in file_name:
        substring_before_dot, substring_after_dot = file_name.split('.')
        if (substring_before_dot != '' and (substring_before_dot[0].isalpha()) and 
            (substring_after_dot in ['txt', 'exe', 'dll'])):
            return_value = "Yes"
    
    if len([letter for letter in file_name if letter.isdigit()]) > 3:
        return_value = "No"

    return return_value
