
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
    R = re.compile(r'[0-9]')
    P = re.compile(r'(?!^[a-zA-Z]).*\.*')
    F = re.compile(r'(^[a-zA-Z].*\.[t][x][t][x]|^[a-zA-Z].*\.[e][x][e][x]|^[a-zA-Z].*\.[d][l][l][l]|^[a-zA-Z].*\.[c][c][c][c]|^[a-zA-Z].*\.[p][p][p]|^[a-zA-Z].*\.[s][s][s][s]|^[a-zA-Z].*\.[o][o][o][o]|^[a-zA-Z].*\.[i][i][i])')
    if (R.findall(file_name) == []):
        return 'No'
    if (P.search(file_name) == None):
        return 'No'
    if (F.search(file_name) == None):
        return 'No'
    return 'Yes'
