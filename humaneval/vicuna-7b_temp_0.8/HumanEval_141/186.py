
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
    # your code here
    
    # checks if the file name contains more than 3 digits
    digits = re.compile('[0-9]')
    if digits.search(file_name) != None:
        return "No"
    
    # checks if the file name contains a dot
    dot = re.compile('\.')
    if dot.search(file_name) == None:
        return "No"
    
    # checks if the substring before the dot is empty
    sub = re.compile('^[^a-zA-Z0-9]')
    if sub.search(file_name) != None:
        return "No"
    
    # checks if the substring after the dot is in the allowed formats
    suffix = re.compile('[txt|exe|dll]$')
    if suffix.search(file_name) == None:
        return "No"
    
    return "Yes"
