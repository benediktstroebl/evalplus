
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

    if len(file_name) > 3 and '0' <= file_name[0] <= '9':
        return 'No'
    else:
        dot_index = file_name.find('.')
        if dot_index == -1:
            return 'No'
        if dot_index == 0:
            return 'No'
        elif dot_index == len(file_name) - 1:
            return 'No'
        else:
            if file_name[dot_index-1]!= 'a' and file_name[dot_index-1]!= 'A':
                return 'No'
            if file_name[dot_index+1] == 'exe':
                return 'No'
            elif file_name[dot_index+1] == 'txt':
                return 'Yes'
            elif file_name[dot_index+1] == 'dll':
                return 'No'
            else:
                return 'No'
