
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
    # check the size
    check = [char for char in file_name if char in '0123456789']
    if len(check) > 3:
        return 'No'
    else:
        # check the dots
        dots = file_name.count('.')
        if dots != 1:
            return 'No'
        else:
            # check the substring
            sub_str = file_name.split('.')
            # check the length
            if len(sub_str[0]) == 0:
                return 'No'
            # check the first char
            if sub_str[0][0] not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                return 'No'
            else:
                # check the extension
                if sub_str[1] not in ['txt', 'exe', 'dll']:
                    return 'No'
                else:
                    return 'Yes'
