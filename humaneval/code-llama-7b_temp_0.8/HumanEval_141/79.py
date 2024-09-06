
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

    valid_extensions = ["txt", "exe", "dll"]
    file_name_list = file_name.split(".")
    if len(file_name_list) == 2 and len(file_name_list[0]) != 0:
        file_extension = file_name_list[1]
        if file_extension in valid_extensions:
            file_name_length = len(file_name_list[0])
            if file_name_length > 3:
                return "No"
            elif file_name_length == 3:
                if file_name_list[0][0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    return "No"
                else:
                    return "Yes"
            else:
                return "Yes"
        else:
            return "No"
    else:
        return "No"
