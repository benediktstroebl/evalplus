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
    no_more_than_three_digits = len(file_name) >= 1 and len(file_name) <= 3
    exactly_one_dot = bool(file_name.count(".")) == 1
    starts_with_letter = file_name[0].isalpha()
    non_empty_before_dot = len(file_name) > 1 and file_name[:-1].isalpha()
    valid_after_dot = set(["txt", "exe", "dll"]) == set(file_name[::-1].split(".")[1:])
    return "Yes" if (no_more_than_three_digits and exactly_one_dot and starts_with_letter and non_empty_before_dot and valid_after_dot) else "No"