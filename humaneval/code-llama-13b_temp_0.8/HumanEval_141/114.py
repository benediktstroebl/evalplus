
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
    # if the file_name has a '.'
    if '.' in file_name:
        # get the substring before the dot
        before_dot = file_name[:file_name.index('.')]
        # get the substring after the dot
        after_dot = file_name[file_name.index('.') + 1:]
        # if the substring before the dot is a valid string
        if before_dot and before_dot[0].isalpha() and before_dot.isalnum() and before_dot.isascii() and before_dot.islower() and before_dot.isupper():
            # if the substring after the dot is in ['txt', 'exe', 'dll']
            if after_dot in ['txt', 'exe', 'dll']:
                # get the number of digits in the file_name
                number_of_digits = 0
                for char in file_name:
                    if char.isdigit():
                        number_of_digits += 1
                # if there are more than three digits
                if number_of_digits <= 3:
                    return 'Yes'
                else:
                    return 'No'
            else:
                return 'No'
        else:
            return 'No'
    else:
        return 'No'
