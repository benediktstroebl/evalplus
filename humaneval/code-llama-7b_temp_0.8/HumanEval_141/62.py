
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

    def count_digits(file_name):
        return sum(s.isdigit() for s in file_name)

    if count_digits(file_name) > 3:
        return 'No'
    elif not file_name.count('.') == 1:
        return 'No'
    elif not file_name[0].isalpha():
        return 'No'
    elif file_name[file_name.find('.')+1:] not in ['txt', 'exe', 'dll']:
        return 'No'
    else:
        return 'Yes'

    # alternatively we could use regular expressions:
    import re

    if not re.match(r'[a-zA-Z]\w*\.\w{3}$', file_name):
        return 'No'
    else:
        return 'Yes'

    # alternatively we could use enumerate:
    count = 0
    for s in file_name:
        if s.isdigit():
            count += 1
            if count > 3:
                return 'No'
        elif s == '.':
            count = 0
    if count != 0:
        return 'No'
    else:
        return 'Yes'

