
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
    
    # Remove spaces and '/' from string
    # file_name = file_name.replace(' ', '')
    # file_name = file_name.replace('/', '')
    
    # Check that the file name contains at most 3 digits
    if len(file_name) > 3:
        return False
        
    # Check that the file name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return False
        
    # Check that the substring before the dot is not empty
    substring = file_name.split('.')[0]
    if len(substring) == 0:
        return False
        
    # Check that the substring after the dot is not empty
    substring = file_name.split('.')[1]
    if len(substring) < 1:
        return False
        
    # Check that the substring is not empty, and starts with a letter from
    # the latin alphapet ('a'-'z' and 'A'-'Z')
    if substring[0].isalpha():
        return True
    else:
        return False

