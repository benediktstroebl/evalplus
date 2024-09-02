
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
    # Define the regular expressions to check the conditions
    REGEX_1 = r'^[a-zA-Z][a-zA-Z0-9]{2}[0-9]$'  # 1st condition
    REGEX_2 = r'^[a-zA-Z][a-zA-Z0-9]*.[a-zA-Z0-9][a-zA-Z0-9]*$'  # 2nd condition
    REGEX_3 = r'^([a-zA-Z][a-zA-Z0-9]*)\.([a-zA-Z\.]*)$'  # 3rd condition
    REGEX_4 = r'^([a-zA-Z][a-zA-Z0-9]*)\.([a-zA-Z\.]*)$'  # 4th condition
    REGEX_5 = r'^([a-zA-Z][a-zA-Z0-9]*)\.([a-zA-Z\.]*)$'  # 5th condition
    
    # Check if the file name matches any of the regular expressions
    if REGEX_1.match(file_name) or REGEX_2.match(file_name) or REGEX_3.match(file_name) or REGEX_4.match(file_name) or REGEX_5.match(file_name):
        return "Yes"
    else:
        return "No"
