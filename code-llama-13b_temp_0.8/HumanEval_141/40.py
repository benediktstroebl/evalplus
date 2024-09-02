
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
    valid_substrings_after_dot = ['txt', 'exe', 'dll']
    counter = 0
    digit_counter = 0
    dot_flag = False
    prev_char_flag = False
    for idx, char in enumerate(file_name):
        if char == '.':
            if dot_flag:
                return 'No'
            dot_flag = True
            continue
        if char == '0':
            if not prev_char_flag:
                return 'No'
            counter += 1
            if counter == 3:
                return 'No'
        if char in valid_substrings_after_dot:
            if char == valid_substrings_after_dot[0] and idx != len(file_name) - 1:
                return 'No'
            return 'Yes'
        if char.isdigit():
            digit_counter += 1
        if char.isdigit() and not dot_flag:
            return 'No'
        if not char.isdigit():
            prev_char_flag = True
    return 'No'
