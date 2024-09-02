
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
    for i in range(len(file_name)):
        if file_name[i] == '.':
            if file_name[i + 1] == '.':
                return 'No'
            else:
                ext = file_name[i + 1:i + 4]
                if ext == 'exe' or ext == 'txt' or ext == 'dll':
                    return 'Yes'
                else:
                    return 'No'
        elif file_name[i].isalpha() or file_name[i].isdigit():
            continue
        else:
            return 'No'
    return 'No'


