
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
    count_letters = 0
    count_digits = 0
    count_dots = 0
    for letter in file_name:
        if letter.isdigit():
            count_digits += 1
        elif letter.isalpha():
            count_letters += 1
        elif letter == '.':
            count_dots += 1
    if count_letters > 0 and count_digits <= 3 and count_dots == 1 and count_letters == 1 and (file_name.endswith("txt") or file_name.endswith("dll") or file_name.endswith("exe")):
        return "Yes"
    else:
        return "No"


