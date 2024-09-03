def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file name is valid if and only if all the following conditions are met:
    - There should not be more than three digits ('0'-'9') in the file's name
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from
    the latin alphabet ('a'-'z' and 'A'-'Z')
    - The substring after the dot is one of these: ['txt', 'exe', 'dll']
    """
    # check the length of the string
    if len(file_name) > 3: return 'No'

    # check if the name has more than one dot
    if '..' in file_name: return 'No'

    # check the first character of the string
    if not file_name[0].isalpha(): return 'No'

    # check the last character of the string
    if not file_name[-1].isalpha(): return 'No'

    # check the substring after the last dot
    if file_name[-2:] not in ['txt', 'exe', 'dll']: return 'Yes'

    return 'No'