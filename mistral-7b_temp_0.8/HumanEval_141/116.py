
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
    counter_digit = 0
    counter_letter = 0
    # check for letters
    for letter in file_name:
        if (letter.isalpha()):
            counter_letter += 1
    if (counter_letter == 1):
        # check for digits
        for digit in file_name:
            if (digit.isdigit()):
                counter_digit += 1
        if (counter_digit > 3):
            return 'No'
    # check for the one dot
    if ('.' in file_name):
        # check for the extension
        if (file_name.endswith('txt') or file_name.endswith('exe') or file_name.endswith('dll')):
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'

