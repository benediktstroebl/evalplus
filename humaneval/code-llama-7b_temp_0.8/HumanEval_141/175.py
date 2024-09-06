
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
    count = 0
    for i in range(len(file_name)):
        if file_name[i] != '.':
            if 97 <= ord(file_name[i]) <= 122 or 65 <= ord(file_name[i]) <= 90:
                continue
            else:
                return 'No'
        elif i == 0:
            return 'No'
        elif i > 0:
            if file_name[i] in ['txt', 'exe', 'dll']:
                continue
            else:
                return 'No'
    for j in range(len(file_name)):
        if ord(file_name[j]) >= 48 and ord(file_name[j]) <= 57:
            count += 1
    if count <= 3:
        return 'Yes'
    else:
        return 'No'

