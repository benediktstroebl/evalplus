
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
    if len(file_name) > 3:
        return "No"
    if file_name.find(".") == -1:
        return "No"
    if file_name[:2].lower() == "0-9":
        return "No"
    if file_name.find(".") < file_name.find("0-9"):
        return "No"
    if file_name.find(".") == 0 and file_name[:2].lower() == "a-z":
        return "No"
    if file_name.find(".") == 0 and file_name[:2].lower() == "A-Z":
        return "No"
    if file_name.find(".") > file_name.find("0-9"):
        extension = file_name.find(".")
        if extension > 1:
            if not extension == 2:
                extension = file_name.find(".", extension + 1)
            if extension == -1:
                return "No"
            if file_name[extension + 1:].lower() not in ["txt", "exe", "dll"]:
                return "No"
        else:
            if file_name.lower().split(".")[1].lower() != "txt" and file_name.lower().split(".")[1].lower() != "exe" and file_name.lower().split(".")[1].lower() != "dll":
                return "No"
    return "Yes"
