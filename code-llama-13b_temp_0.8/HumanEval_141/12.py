
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
    count=0
    if file_name.count('.')>1:
        return 'No'
    if file_name.startswith('.') or file_name.endswith('.'):
        return 'No'
    if file_name.startswith('a') or file_name.startswith('z') or file_name.startswith('A') or file_name.startswith('Z'):
        return 'No'
    if file_name.endswith('exe') or file_name.endswith('txt') or file_name.endswith('dll'):
        return 'No'
    if file_name.startswith('1') or file_name.startswith('2') or file_name.startswith('3') or file_name.startswith('4') or file_name.startswith('5') or file_name.startswith('6') or file_name.startswith('7') or file_name.startswith('8') or file_name.startswith('9'):
        return 'No'
    if file_name.startswith('0') or file_name.startswith('1') or file_name.startswith('2') or file_name.startswith('3') or file_name.startswith('4') or file_name.startswith('5') or file_name.startswith('6') or file_name.startswith('7') or file_name.startswith('8') or file_name.startswith('9'):
        return 'No'
    if file_name.endswith('exe') or file_name.endswith('txt') or file_name.endswith('dll'):
        return 'No'
    for i in range(0,len(file_name)):
        if file_name[i]=='.' and file_name[i+1]=='.':
            return 'No'
    return 'Yes'
    
