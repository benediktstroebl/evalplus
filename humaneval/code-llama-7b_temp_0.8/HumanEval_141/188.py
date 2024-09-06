
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
    # my solution
    file_name = file_name.split(".")
    if file_name[0].isalpha() == False:
        return "No"
    elif file_name[0].isdigit():
        return "No"
    elif len(file_name) > 2:
        return "No"
    elif len(file_name) == 1:
        return "No"
    elif file_name[-1].lower() not in ["txt", "exe", "dll"]:
        return "No"
    else:
        return "Yes"
    
    # leetcode solution
    # import re
    # return 'Yes' if re.search(r'^\w+\.\w{3}$', file_name) else 'No'
    
    # one line solution
    # return 'Yes' if file_name.count('.') == 1 and file_name.count(' ') == 0 and file_name.split('.')[-1] in ['txt', 'exe', 'dll'] and file_name.split('.')[0][0].isalpha() and file_name.split('.')[0][0] != '.' and not file_name.split('.')[0][-1].isdigit() and not file_name.split('.')[0][0].isdigit() else 'No'
    
    
    
