
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
    # return 'No' if the file name does not contain a dot
    if not "." in file_name:
        return "No"
    
    # return 'No' if the file name contains more than one dot
    if file_name.count(".") > 1:
        return "No"
    
    # return 'No' if the substring before the dot starts with a non-alphapet character
    if not file_name[0].isalpha():
        return "No"
    
    # return 'No' if the substring after the dot is not one of these: ['txt', 'exe', 'dll']
    if not file_name.split(".")[-1] in ["txt", "exe", "dll"]:
        return "No"
    
    # return 'No' if there is more than three digits in the file name
    if len([i for i in file_name if i.isdigit()]) > 3:
        return "No"
    
    return "Yes"
