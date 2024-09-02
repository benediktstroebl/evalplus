
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
    # STRATEGY:
    # 1. Validate the file name
    # 2. Return the result to the caller

    # 1. Validate the file name
    # 1.1. Split the file name into substrings before and after the dot separator
    file_name_parts = file_name.split(".")

    # 1.2. Validate the file name parts
    # 1.2.1. Validate that the file name contains exactly one dot
    if len(file_name_parts) != 2:
        return "No"

    # 1.2.2. Validate that the file name before the dot is valid
    # 1.2.2.1. Validate that the file name before the dot contains at least one character
    if len(file_name_parts[0]) == 0:
        return "No"

    # 1.2.2.2. Validate that the file name before the dot contains only letters from the latin alphapet
    if not file_name_parts[0][0].isalpha():
        return "No"

    # 1.2.3. Validate that the file name after the dot is valid
    # 1.2.3.1. Validate that the file name after the dot contains one of the three specified file types
    if file_name_parts[1] not in ["txt", "exe", "dll"]:
        return "No"

    # 1.2.4. Validate that the file name after the dot contains at most three digits
    # 1.2.4.1. If the file name contains no digits, return 'Yes'
    if not any([char.isdigit() for char in file_name_parts[1]]):
        return "Yes"

    # 1.2.4.2. If the file name contains digits, validate the number of digits is less than three
    # 1.2.4.2.1. Get the number of digits in the file name
    number_of_digits = sum([char.isdigit() for char in file_name_parts[1]])

    # 1.2.4.2.2.
