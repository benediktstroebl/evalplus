
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
    # your code goes here
    if file_name.count(".") > 1:
        return "No"
    temp = file_name.split(".")
    if len(temp[0]) == 0:
        return "No"
    if not(temp[0][0].isalpha()):
        return "No"
    if len(temp[0].split(" ")) > 1:
        return "No"
    if len(temp[0].split("0")) > 4 or len(temp[0].split("1")) > 4 or len(temp[0].split("2")) > 4 or len(temp[0].split("3")) > 4 or len(temp[0].split("4")) > 4 or len(temp[0].split("5")) > 4 or len(temp[0].split("6")) > 4 or len(temp[0].split("7")) > 4 or len(temp[0].split("8")) > 4 or len(temp[0].split("9")) > 4:
        return "No"
    if temp[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
    
    
