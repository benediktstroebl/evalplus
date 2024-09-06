
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
    # import re
    # return 'No' if len(re.findall(r'\d', file_name)) > 3 or re.search(r'\.', file_name) == None or re.search(r'[a-zA-Z]', file_name[0]) == None or not file_name.lower().endswith(('.txt', '.exe', '.dll')) else 'Yes'

    #Check if there are more than 3 digits in the file name
    if file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3:
        return 'No'
    
    #Check if there is only one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    
    #Check if the file name starts with a letter
    if file_name[0].isalpha() == False:
        return 'No'
    
    #Check if the file name ends with one of the extensions
    if file_name.lower().endswith('.txt') == False and file_name.lower().endswith('.exe') == False and file_name.lower().endswith('.dll') == False:
        return 'No'
    
    return 'Yes'
