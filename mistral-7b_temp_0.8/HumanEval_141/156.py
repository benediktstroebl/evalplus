
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
    number = 0
    dot = 0
    letter = 0
    extension = 0
    for letter_index in file_name:
        if letter_index.isdigit():
            number += 1
    for dot_index in file_name:
        if dot_index == ".":
            dot += 1
    for letter_index in file_name:
        if letter_index.isalpha():
            letter += 1
    for extension_index in file_name:
        if extension_index in ["txt", "exe", "dll"]:
            extension += 1
    if number > 3 or dot < 1 or letter < 1 or extension < 1:
        return "No"
    else:
        return "Yes"


