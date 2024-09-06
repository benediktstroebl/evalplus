
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
    counter = 0
    for i in file_name:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            counter += 1
        if counter > 3:
            return "No"

    if "." not in file_name:
        return "No"
    elif file_name[0] == ".":
        return "No"
    else:
        substring = file_name.split(".")
        if "" in substring:
            return "No"

    if (substring[-1] == "txt") or (substring[-1] == "exe") or (substring[-1] == "dll"):
        return "Yes"
    else:
        return "No"
