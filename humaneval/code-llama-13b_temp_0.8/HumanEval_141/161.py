
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
    # 1st solution
    # lst = list(filter(lambda x: x.isdigit(), file_name))
    # return 'Yes' if len(lst) <= 3 and file_name.count(".") == 1 and file_name[:file_name.index(".")].isalpha() and file_name[file_name.index(".")+1:] in ["txt", "exe", "dll"] else 'No'

    # 2nd solution
    # return 'Yes' if len(file_name.split(".")[0]) != 0 and file_name.count(".") == 1 and file_name.split(".")[0][0].isalpha() and file_name.split(".")[-1] in ["txt", "exe", "dll"] else 'No'
    
    # 3rd solution
    if len(file_name.split(".")[0]) != 0 and file_name.count(".") == 1 and file_name.split(".")[0][0].isalpha() and file_name.split(".")[-1] in ["txt", "exe", "dll"] and len(list(filter(lambda x: x.isdigit(), file_name))) <= 3:
        return "Yes"
    else:
        return "No"
