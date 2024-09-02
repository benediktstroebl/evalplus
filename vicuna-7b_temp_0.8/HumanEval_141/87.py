
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
    # 1. Check if the file's name contains more than three digits
    if len(file_name) > 3:
        return "No"
    
    # 2. Check if the file's name contains a dot
    if ".txt" not in file_name or ".exe" not in file_name or ".dll" not in file_name:
        return "No"
    
    # 3. Check if the substring before the dot is empty or starts with a letter from the latin alphabet
    if not file_name.startswith(string.ascii_letters) or not file_name or ".txt" not in file_name:
        return "No"
    
    # 4. Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if file_name.split(".")[-1] != "txt" and file_name.split(".")[-1] != "exe" and file_name.split(".")[-1] != "dll":
        return "No"
    
    # If all the above conditions are met, the file's name is valid and the function returns "Yes"
    return "Yes"
