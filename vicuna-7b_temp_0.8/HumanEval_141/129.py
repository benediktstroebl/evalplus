
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
    # Get the file name
    file_name = file_name.lower()

    # Check for three digits
    if sum([ord(c) - ord('0') for c in file_name]) > 3:
        return "No"

    # Check for dot
    if not file_name.endswith(".txt") and not file_name.endswith(".exe") and not file_name.endswith(".dll"):
        return "No"

    # Get the substring before the dot
    before_dot = file_name[:len(file_name) - 3]

    # Check for letter
    if not any(c.isalnum() for c in before_dot):
        return "No"

    # Get the substring after the dot
    after_dot = file_name[len(file_name) - 3:]

    # Check for allowed extensions
    if not after_dot.startswith(["txt", "exe", "dll"]):
        return "No"

    return "Yes"
