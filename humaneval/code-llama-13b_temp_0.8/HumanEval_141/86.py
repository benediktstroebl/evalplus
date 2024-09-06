
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
    ### START CODE HERE ###

    # Create a regular expression to check if the file's name is valid
    regex = r"^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z0-9]{1,3}){0,1}$"

    # If the file's name matches the regular expression, return 'Yes', otherwise return 'No'
    return 'Yes' if re.match(regex, file_name) else 'No'

    ### END CODE HERE ###
    
