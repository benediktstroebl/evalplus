
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
    substring_before_dot = ''
    substring_after_dot = ''
    result = None
    for letter in file_name:
        if 48 <= ord(letter) <= 57:
            if len(substring_before_dot) <= 3:
                substring_before_dot += letter
            else:
                result = 'No'
        elif 97 <= ord(letter) <= 122:
            if len(substring_before_dot) > 0:
                result = 'No'
                break
            else:
                substring_before_dot += letter
        elif ord(letter) == 46:
            if len(substring_before_dot) > 0:
                if len(substring_after_dot) <= 0:
                    substring_after_dot += letter
                else:
                    result = 'No'
                    break
            else:
                result = 'No'
                break
        elif ord(letter) == 32:
            if len(substring_before_dot)
