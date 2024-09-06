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
    if not isinstance(file_name, str):
        return "File name should be a string!"

    latin_letter = False
    num_digits = 0
    dot_index = -1
    suffix = ""

    for char in file_name:
        if char.isdigit():
            num_digits += 1
        elif char == ".":
            dot_index = len(file_name) - 1
        elif ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")):
            latin_letter = True
        else:
            suffix += char

    if num_digits > 3 or (dot_index == -1) or (not latin_letter):
        return "No"
    elif suffix not in ["txt", "exe", "dll"]:
        return "No"
    else:
        return "Yes"