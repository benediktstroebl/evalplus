
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

    if file_name.count(".") > 1:
        return "No"

    before_dot = file_name.split(".")[0]
    after_dot = file_name.split(".")[1]

    if not (97 <= ord(before_dot[0]) <= 122 or 65 <= ord(before_dot[0]) <= 90):
        return "No"

    if before_dot == "":
        return "No"

    if after_dot not in ("txt", "exe", "dll"):
        return "No"

    if sum(map(lambda x: 48 <= ord(x) <= 57, before_dot)) > 3:
        return "No"

    return "Yes"
