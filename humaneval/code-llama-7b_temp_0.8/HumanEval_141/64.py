
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
    # Replace all the numbers
    file_name_no_nums = ''.join([letter for letter in file_name if not letter.isdigit()])

    # Split at the dot
    file_name_split = file_name_no_nums.split('.')

    # Check that the file has more than one part
    if len(file_name_split) < 2:
        return 'No'

    # Extract the first part of the file
    file_name_pre = file_name_split[0]

    # Check that the file name starts with a letter
    if not file_name_pre[0].isalpha():
        return 'No'

    # Check that the extension is valid
    if file_name_split[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
