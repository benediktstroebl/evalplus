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
    
    if len(file_name) == 0:
        return "File name should not be empty"
    
    counter = 0
    for char in file_name:
        if char == ".":
            counter += 1
        elif char >= "0" and char <= "9":
            counter += 1
    
    if counter > 3:
        return "File name should not have more than three digits"
    elif counter != 1:
        return "File name should contain exactly one dot"
    
    pos = file_name.find(".")
    if pos == -1:
        return "File name should contain exactly one dot"
    
    if file_name[:pos] == "":
        return "File name substring before dot should not be empty"
    
    if not file_name[:pos].isalpha():
        return "File name substring before dot should start with a letter from the latin alphabet"
    
    ext = file_name[pos+1:]
    valid_ext = ["txt", "exe", "dll"]
    if ext not in valid_ext:
        return "File name substring after dot should be one of these: ['txt', 'exe', 'dll']"
    
    return "Yes"