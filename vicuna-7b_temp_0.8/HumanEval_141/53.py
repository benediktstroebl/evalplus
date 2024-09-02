
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
    # regex pattern to check for valid file names
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9]+\.(?:[a-zA-Z]+|[a-zA-Z0-9]+\.)\s*[a-zA-Z]{2,}$')
    
    # check if the file name contains only digits
    if re.search(r'^[0-9]+$', file_name) != None:
        return 'No'
    
    # check if the file name contains exactly one dot
    if re.search(r'\.(?:[a-zA-Z]+|[a-zA-Z0-9]+\.)\s*[a-zA-Z]{2,}$', file_name) != None:
        return 'No'
    
    # check if the substring before the dot is empty or starts with a letter
    if re.search(r'\b[a-zA-Z]+\.?\s*[a-zA-Z0-9]*$', file_name) == None:
        return 'No'
    
    # check if the substring after the dot is one of the allowed extensions
    if not re.search(r'\b[aeiou]+\b', file_name) and re.search(r'^[a-zA-Z]+$', file_name) and re.search(r'\.(?:txt|exe|dll)$', file_name):
        return 'Yes'
    else:
        return 'No'