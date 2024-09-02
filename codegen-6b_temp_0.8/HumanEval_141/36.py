
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
    file_name = file_name.lower()
    name_error_message = "({}) You have a bad file name: {}"

    max_chars = 4
    if len(file_name) > max_chars:
        raise ValueError(name_error_message.format(
            "too many", file_name.title()))

    if file_name.find('.') == -1:
        raise ValueError(name_error_message.format(
            "no dot", file_name.title()))

    if file_name[0].isalpha() != True:
        raise ValueError(name_error_message.format(
            "not start with letter", file_name.title()))

    last_char = file_name.split('.')[1]

    if last_char not in ['exe', 'dll', 'txt']:
        raise ValueError(name_error_message.format(
            "last char invalid", file_name.title()))

    return "Yes"

