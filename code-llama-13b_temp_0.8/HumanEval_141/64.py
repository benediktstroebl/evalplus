
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
    lst=file_name.split(".")
    if len(lst[0])==0:
        return 'No'
    if ord(lst[0][0])>64 and ord(lst[0][0])<91 or ord(lst[0][0])>96 and ord(lst[0][0])<123:
        pass
    else:
        return 'No'
    if lst[1] in ['txt','exe','dll']:
        pass
    else:
        return 'No'
    for x in lst[0]:
        if ord(x)>=48 and ord(x)<=57:
            count=count+1
    if count>3:
        return 'No'
    return 'Yes'










