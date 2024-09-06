
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
    # pass
    digits = 0
    dot = 0
    # letters = 0
    sub_1 = file_name[:file_name.index(".")]
    sub_2 = file_name[file_name.index(".")+1:]
    if "." in file_name:
        dot += 1
    if sub_1 == "":
        return "No"
    if len(file_name) > 3:
        for i in file_name:
            if i.isdigit():
                digits += 1
        if digits > 3:
            return "No"
    if sub_1[0].isalpha() == False:
        return "No"
    if sub_2 not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
