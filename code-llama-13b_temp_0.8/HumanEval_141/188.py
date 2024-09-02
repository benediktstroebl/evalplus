
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

    # valid_name = "name"
    # valid_name = ".file"
    # valid_name = ".file."
    # valid_name = ".txt"
    # valid_name = "a.exe"
    # valid_name = "a.dll"
    # valid_name = "a.s.exe"
    # valid_name = "a.txt"
    # valid_name = ".dll"
    # valid_name = "a.a.exe"
    # valid_name = "a.s.s.txt"
    # valid_name = ".exe"
    # valid_name = "aaa.exe"
    # valid_name = ".txt"
    # valid_name = "aaa.dll"
    # valid_name = ".s.txt"
    # valid_name = "a.a.a.a.txt"
    # valid_name = ".exe"
    # valid_name = "a.dll"
    # valid_name = "a.txt"
    # valid_name = "a.exe"
    # valid_name = "1.exe"
    # valid_name = "11.exe"
    # valid_name = "111.exe"
    # valid_name = "1111.exe"
    # valid_name = "1111.txt"
    # valid_name = "111.txt"
    # valid_name = "11.txt"
    # valid_name = "1.txt"
    # valid_name = ".txt"

    # return 'Yes' if the the file's name is valid, and returns 'No' otherwise.
    return 'Yes' if len(re.findall('[0-9]', file_name)) <= 3 and '.' in file_name and file_name.split('.')[0] and file_name.split('.')[1] in ['txt', 'exe', 'dll'] else 'No'
    pass
