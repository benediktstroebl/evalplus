
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
    if file_name.count(".") > 1:
        return "No"
    else:
        if (file_name.count(".") == 1) and (file_name.count("0") < 4) and (file_name.count("1") < 4) and (file_name.count("2") < 4) and (file_name.count("3") < 4) and (file_name.count("4") < 4) and (file_name.count("5") < 4) and (file_name.count("6") < 4) and (file_name.count("7") < 4) and (file_name.count("8") < 4) and (file_name.count("9") < 4):
            if file_name[0].isalpha() == False:
                return "No"
            elif file_name[0].isdigit() == True:
                return "No"
            elif file_name.count(".") == 1 and (file_name[-3:].lower() != "exe") and (file_name[-3:].lower() != "txt") and (file_name[-3:].lower() != "dll"):
                return "No"
            elif file_name[-3:].lower() == "exe" or file_name[-3:].lower() == "txt" or file_name[-3:].lower() == "dll":
                return "Yes"
            else:
                return "No"
        else:
            return "No"
