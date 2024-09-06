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

    if not file_name.isalpha():
        return "Invalid file name! The name should start with a letter."

    parts = file_name.split(".")

    if len(parts) != 2: 
        return "Invalid file name! The file name should contain exactly one dot."

    prefix = parts[0]
    suffix = parts[1]

    if prefix == "":
        return "Invalid file name! The prefix cannot be empty."

    if not prefix.isalpha():
        return "Invalid file name! The prefix should start with a letter."

    if suffix not in ["txt", "exe", "dll"]:
        return "Invalid file name! The suffix should be one of ['txt', 'exe', 'dll']."

    digits = prefix.count("0123456789")
    if digits > 3:
        return "Invalid file name! There should not be more than three digits in the file name."

    return "Yes"