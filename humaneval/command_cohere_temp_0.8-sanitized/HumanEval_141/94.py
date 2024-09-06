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
    if not isinstance(file_name, str):
        return "File name should be a string"

    if not file_name.startswith(tuple('aeiouAEIOU')):
        return "File name should start with a letter"

    latin_letter = file_name[0]
    ext = file_name.split(".")[1].lower() if "." in file_name else ""
    
    if len(set(file_name) & set("0123456789")) > 3:
        return "More than three digits in file name"

    if len(file_name.split(".")) != 2:
        return "Invalid file name. No dot '.'"

    if ext not in ['txt', 'exe', 'dll']:
        return "File extension should be either 'txt', 'exe' or 'dll'"

    return "Yes"