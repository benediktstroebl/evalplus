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
    if not file_name or not isinstance(file_name, str):
        return "Yes"

    # Ensure there are no more than 3 digits
    if re.search(r'\d{4}', file_name):
        return "No"

    # Ensure there is exactly 1 dot
    if ".." in file_name or "." in file_name:
        return "No"

    # Ensure the substring before the dot matches criteria
    if not file_name.startswith(tuple(char.lower() for char in list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))):
        return "No"

    # Ensure the substring after the dot is either "txt", "exe" or "dll"
    if file_name.split(".")[-1].lower() not in ["txt", "exe", "dll"]:
        return "No"
    
    return "Yes"