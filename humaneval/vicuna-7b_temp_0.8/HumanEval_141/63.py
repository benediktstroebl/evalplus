
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
    # Define regular expressions to match the different conditions
    reg1 = re.compile(r'^[a-zA-Z0-9]*[0-9]?$')
    reg2 = re.compile(r'^[a-zA-Z0-9]*\.([a-zA-Z0-9]*|[a-zA-Z0-9]*\.?[a-zA-Z0-9]*)[a-zA-Z]{2,}$')
    reg3 = re.compile(r'([a-zA-Z0-9]*)\.([a-zA-Z0-9]*\.([a-zA-Z0-9]*|[a-zA-Z0-9]*\.?[a-zA-Z0-9]*)|([a-zA-Z0-9]+\..+[a-zA-Z0-9]*))')
    reg4 = re.compile(r'^[a-zA-Z0-9]*\.([a-zA-Z0-9]*|[a-zA-Z0-9]*\.?[a-zA-Z0-9]*)[a-zA-Z]{2,}$')

    # Use the regexp pattern matching to check if the file name matches the conditions
    if reg1.match(file_name) is not None:
        return "Yes"
    elif reg2.match(file_name) is not None:
        if not reg2.match(file_name).group(1).isalpha():
            return "No"
        else:
            return "Yes"
    elif reg3.match(file_name) is not None:
        if not reg3.match(file_name).group(1).isalpha():
            return "No"
        elif not reg3.match(file_name).group(2).isalpha():
            return "No"
        elif not reg3.match(file_name).group(3).isalpha():
            return "No"
        elif not reg3.match(file_name).group(4).isalpha():
            return "No"
        else:
            return "Yes"
    elif reg4.match(file_name) is not None:
        if
