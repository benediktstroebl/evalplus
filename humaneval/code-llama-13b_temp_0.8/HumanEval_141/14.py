
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
    # if there is more than three numbers and one dot and is not a valid letter return 'No'
    if file_name.count(".") != 1 or not file_name[0].isalpha() or file_name.count("0123456789") > 3:
        return 'No'
    #split the file name
    string_split = file_name.split(".")
    #check if the second part of the split is correct
    if string_split[1] != "txt" and string_split[1] != "exe" and string_split[1] != "dll":
        return 'No'
    #if nothing is wrong return yes
    return 'Yes'
