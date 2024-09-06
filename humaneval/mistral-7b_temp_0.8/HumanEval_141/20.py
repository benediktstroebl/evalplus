
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
    file_name_list = file_name.split('.')
    #number of digits in the file's name
    num_digits = 0
    for digit in file_name:
        if digit.isdigit():
            num_digits += 1
    #number of characters in the file's name
    num_chars = 0
    for char in file_name:
        if char.isalnum():
            num_chars += 1
    #number of periods in the file's name
    num_dots = 0
    for dot in file_name:
        if dot == '.':
            num_dots += 1
    if len(file_name_list) > 1 and (file_name_list[0] != ''):
        if len(file_name) > 0:
            if num_digits <= 3 and num_dots == 1 and num_chars == 1 and (file_name_list[1] == 'txt' or file_name_list[1] == 'exe' or file_name_list[1] ==
