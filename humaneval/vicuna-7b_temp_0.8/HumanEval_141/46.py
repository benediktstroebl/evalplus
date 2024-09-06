
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
    # Check if the name has more than 3 digits
    if len(file_name) > 3:
        return "No"
    
    # Check if the name contains exactly one dot
    if file_name.find(".") != file_name.find(" ") and file_name.find(".") != file_name.rfind("."):
        return "No"
    
    # Check if the substring before the dot is a letter
    if file_name.find(".") == file_name.find(" ") or file_name.find(".") == file_name.rfind("."):
        return "No"
    else:
        start_index = file_name.find("[a-zA-Z]")
        if start_index == -1:
            return "No"
        else:
            end_index = file_name.find(".", start_index)
            if end_index == -1:
                return "No"
            else:
                extension = file_name[end_index:].split(".")[-1]
                if extension not in ["txt", "exe", "dll"]:
                    return "No"
                else:
                    return "Yes"