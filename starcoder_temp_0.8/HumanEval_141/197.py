
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
    count = 0
    count_alpha = 0
    for letter in file_name:
        if ord(letter) > 47 and ord(letter) < 58:
            count += 1
        elif ord(letter) > 96 and ord(letter) < 123:
            count_alpha += 1
    if count > 3 or count_alpha == 0:
        return "No"
    if file_name.count(".")!= 1:
        return "No"
    else:
        if file_name[0] == ".":
            return "No"
        if file_name[file_name.index(".")] == ".":
            return "No"
        else:
            s = file_name[file_name.index(".") + 1:]
            if s not in ['txt', 'exe', 'dll']:
                return "No"
            else:
                return "Yes"
