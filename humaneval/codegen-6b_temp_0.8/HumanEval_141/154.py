
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
    # We first check if the file name has more than 3 digits.
    # NOTE: We cannot use a string's 'contains' method to check if the string contains digits.
    # Because it checks the substring with every digit, so the file_name_check('1example.dll') will 
    # return 'Yes' until the program is finished with it.
    # If the file name has more than 3 digits, we don't know whether the file name is valid or not.
    # We need to consider this case in the logic.
    if len(file_name) > 3:
        return 'No'
    # We now check if the file name has exactly one dot
    # NOTE: We cannot use 'in' method to check if a string contains a specific substring.
    # Because it checks the substring with every substring, so the file_name_check('1example.dll')
    # will return 'No' until the program is finished with it.
    # If the file name has exactly one dot, we don't know whether the file name is valid or not.
    # We need to consider this case in the logic.
    if '.' not in file_name:
        return 'No'
    # Now we check if the substring before the dot is not empty.
    # NOTE: We cannot use 'in' method to check if a string contains a specific substring.
    # Because it checks the substring with every substring, so the file_name_check('1example.dll')
    # will return 'No' until the program is finished with it.
    # If the substring before the dot is empty, we don't know whether the file name is valid or not.
    # We need to consider this case in the logic.
    if file_name[0] not in 'abcdefghijklmnopqrstuvwxyz':
        return 'No'
    # Now we check if the substring after the dot is not empty.
    # NOTE: We cannot use 'in' method to check if a string contains a specific substring.
    # Because it checks the substring with every substring, so the file_name_check('1example.dll')
    # will return 'No' until the program is finished with it.