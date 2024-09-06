
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
    # Test if the file name contains only digits
    if re.match(r'^[0-9]+$', file_name):
        return "No"

    # Test if the file name contains a dot
    if file_name.find('.') < 0:
        return "No"

    # Test if the substring before the dot is empty
    if re.match(r'^\W+', file_name[:file_name.find('.')]).groups()[0]:
        return "No"

    # Test if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if not re.match(r'^[aeiou]+\w+$', file_name[file_name.find('.')+1:]) in [r'txt', r'exe', r'dll']:
        return "No"

    return "Yes"
