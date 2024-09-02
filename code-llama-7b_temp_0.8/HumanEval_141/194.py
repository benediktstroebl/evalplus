
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

    # Create empty string
    file_name_string = ''

    # Create a loop which will check if there are more than three digits in the file name
    for i in range(len(file_name)):
        if (file_name[i] != '.') and (file_name[i] != ' '):
            if file_name[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                return 'No'
            else:
                file_name_string += file_name[i]
        elif (file_name[i] == '.') and (file_name[i+1] in ('txt', 'exe', 'dll')):
            return 'Yes'

    # If the file name is not valid, then return 'No'
    if len(file_name_string) == 0:
        return 'No'

    # If the file name is valid, then return 'Yes'
    elif len(file_name_string) > 0:
        return 'Yes'


