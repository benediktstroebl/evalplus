
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
    import re

    regex_num = re.compile(r'[0-9]{1,3}')
    regex_dot = re.compile(r'\.')
    regex_text = re.compile(r'txt$|exe$|dll$')
    regex_first_letter = re.compile(r'[a-zA-Z]')
    if len(file_name) > 3:
        return 'No'
    elif not regex_dot.match(file_name) or not regex_first_letter.match(file_name):
        return 'No'
    elif not regex_num.match(file_name) and not regex_text.match(file_name):
        return 'No'
    else:
        return 'Yes'
