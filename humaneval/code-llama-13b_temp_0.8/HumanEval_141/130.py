
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
    #your code here
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sub = file_name.split(".")
    if len(sub[0]) == 0 or len(sub) > 2:
        return "No"
    if sub[0][0] not in alpha:
        return "No"
    if len(sub[0].split(" ")) > 1 or sub[0][-1] == " ":
        return "No"
    if len(sub[0].split("0")) - 1 > 3 or len(sub[0].split("1")) - 1 > 3 or len(sub[0].split("2")) - 1 > 3 or len(sub[0].split("3")) - 1 > 3 or len(sub[0].split("4")) - 1 > 3 or len(sub[0].split("5")) - 1 > 3 or len(sub[0].split("6")) - 1 > 3 or len(sub[0].split("7")) - 1 > 3 or len(sub[0].split("8")) - 1 > 3 or len(sub[0].split("9")) - 1 > 3:
        return "No"
    if sub[1] != "txt" and sub[1] != "exe" and sub[1] != "dll":
        return "No"
    return "Yes"
    pass
