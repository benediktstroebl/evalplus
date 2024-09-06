
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
    # your code here
    if len(file_name) > 1:
        if file_name.count(".") == 1:
            if file_name.count(".") < 2:
                if len(file_name[:file_name.index(".")]) > 0:
                    if file_name[0].isalpha():
                        if file_name[file_name.index(".") + 1:].lower() in ['txt', 'exe', 'dll']:
                            if file_name[:file_name.index(".")].count("0") + file_name[:file_name.index(".")].count("1") + file_name[:file_name.index(".")].count("2") + file_name[:file_name.index(".")].count("3") + file_name[:file_name.index(".")].count("4") + file_name[:file_name.index(".")].count("5") + file_name[:file_name.index(".")].count("6") + file_name[:file_name.index(".")].count("7") + file_name[:file_name.index(".")].count("8") + file_name[:file_name.index(".")].count("9") == 0:
                                return "Yes"
                            else:
                                return "No"
                        else:
                            return "No"
                    else:
                        return "No"
                else:
                    return "No"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"
