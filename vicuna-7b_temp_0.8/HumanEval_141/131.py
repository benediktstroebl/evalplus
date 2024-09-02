
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
    invalid_chars = r'[0-9]'
    invalid_chars_dot = r'[0-9]'
    invalid_chars_dot_letter = r'[a-zA-Z]'
    invalid_chars_dot_letter_txt = r'[a-zA-Z][a-zA-Z][a-zA-Z]'

    invalid_file_name = re.sub(invalid_chars, invalid_chars_dot, file_name)
    invalid_file_name = re.sub(invalid_chars_dot, invalid_chars_dot_letter, invalid_file_name)
    invalid_file_name = re.sub(invalid_chars_dot_letter, invalid_chars_dot_letter_txt, invalid_file_name)

    return True if re.match(r'.*\.([txt]exe|dll)$', invalid_file_name) else False
