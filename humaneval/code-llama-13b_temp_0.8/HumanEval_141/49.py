
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
    # if file_name.count('.')>1 or file_name.count('.')<1:
    #     return "No"
    # if file_name[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    #     return "No"
    # if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
    #     return "No"
    # if len(file_name[:file_name.find('.')])==0:
    #     return "No"
    # if len(file_name.replace('.', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', ''))==0:
    #     return "No"
    # return "Yes"
    return ("Yes" if file_name.count('.')==1 and file_name[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and file_name.split('.')[1] in ['txt', 'exe', 'dll'] and len(file_name[:file_name.find('.')])>0 and len(file_name.replace('.', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', ''))>0 else "No")
