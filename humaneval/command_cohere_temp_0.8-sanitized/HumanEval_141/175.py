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
    if not file_name or not isinstance(file_name, str):
        return "Yes"

    # Ensure there are no more than 3 digits
    if digit_count(file_name) > 3:
        return "No"

    # Ensure there is exactly 1 dot
    if dot_count(file_name) != 1:
        return "No"

    # Ensure the substring before the dot starts with a letter
    if not letter_check(file_name):
        return "No"

    # Ensure the substring after the dot is in the list
    if file_extension(file_name) not in ["txt", "exe", "dll"]:
        return "No"

    return "Yes"
def digit_count(file_name):
    return sum(1 for char in file_name if char.isdigit())
def dot_count(file_name):
    return file_name.count(".")
def file_extension(file_name):
    return file_name.split(".")[1]
def letter_check(file_name):
    return bool(file_name[0].lower() == file_name[0])