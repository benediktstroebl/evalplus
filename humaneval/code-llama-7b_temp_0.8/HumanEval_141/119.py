
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
    if file_name.count(".") == 1:
        if file_name.index(".") > 1:
            return "No"
    if file_name.count(".") == 0:
        if file_name.index(".") != -1:
            return "No"
    if file_name.count(".") == 1:
        if file_name.count("0") > 1 or file_name.count("1") > 1 or file_name.count("2") > 1 or file_name.count("3") > 1 or file_name.count("4") > 1 or file_name.count("5") > 1 or file_name.count("6") > 1 or file_name.count("7") > 1 or file_name.count("8") > 1 or file_name.count("9") > 1:
            return "No"
        if not file_name[0].isalpha():
            return "No"
        if file_name[-4:] != ".txt" and file_name[-4:] != ".exe" and file_name[-4:] != ".dll":
            return "No"
    if file_name.count(".") == 0:
        if file_name[0].isalpha():
            if file_name[-4:] == ".txt" or file_name[-4:] == ".exe" or file_name[-4:] == ".dll":
                return "Yes"
            else:
                return "No"
        else:
            return "No"
    if file_name.count(".") == 1:
        if file_name[0].isalpha():
            if file_name[-4:] == ".txt" or file_name[-4:] == ".exe" or file_name[-4:] == ".dll":
                return "Yes"
            else:
                return "No"
        else:
            return "No"
