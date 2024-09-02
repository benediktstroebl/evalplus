
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
    # my solution
    for ch in file_name:
        if ch.isdigit() and file_name.count(ch) > 3:
            return "No"
    if "." not in file_name:
        return "No"
    if not file_name[0].isalpha():
        return "No"
    if not file_name[-4:] in (".txt", ".exe", ".dll"):
        return "No"
    return "Yes"
    # best way
    # return "Yes" if 3 > sum(c.isdigit() for c in file_name) and file_name.count(".") == 1 and file_name[-4:].lower() in (".txt", ".exe", ".dll") and file_name[:1].isalpha() else "No"
