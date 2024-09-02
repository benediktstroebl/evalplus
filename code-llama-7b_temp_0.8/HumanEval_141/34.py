
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
    # check if there are more than three digits in the file name
    # check if there is no period in the file name
    # check if the first part of the file name has more than one letter
    # check if the last part of the file name is not txt, exe, or dll
    # return Yes if all conditions are met, else No

    if file_name.isalnum() == False:
        return "No"
    elif file_name.find(".") == -1:
        return "No"
    elif file_name[0].isalpha() == False:
        return "No"
    elif file_name[file_name.find(".") + 1:].find("txt") == -1 and file_name[file_name.find(".") + 1:].find("exe") == -1 and file_name[file_name.find(".") + 1:].find("dll") == -1:
        return "No"
    else:
        return "Yes"


