
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
    #import re
    #return str(bool(re.match(r"^[a-zA-Z]+([0-9]|\.|[a-zA-Z]\.|[0-9][a-zA-Z]\.)",file_name)))
    list_of_file_names = file_name.split(".")
    if file_name.count(".") != 1:
        return "No"
    elif not file_name[0].isalpha():
        return "No"
    elif file_name.count("0") > 3 or file_name.count("1") > 3 or file_name.count("2") > 3 or file_name.count("3") > 3 or file_name.count("4") > 3 or file_name.count("5") > 3 or file_name.count("6") > 3 or file_name.count("7") > 3 or file_name.count("8") > 3 or file_name.count("9") > 3:
        return "No"
    elif len(list_of_file_names[0]) == 0:
        return "No"
    elif not (list_of_file_names[1] == "txt" or list_of_file_names[1] == "exe" or list_of_file_names[1] == "dll"):
        return "No"
    else:
        return "Yes"
