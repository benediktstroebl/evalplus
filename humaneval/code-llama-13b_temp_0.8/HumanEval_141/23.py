
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
    # 1) If the length of the string is less than 1, return 'No'
    if len(file_name) < 1:
        return 'No'
    
    # 2) Count the number of digits in the file name
    num_of_digits = 0
    for i in file_name:
        if (ord(i) >= 48) and (ord(i) <= 57):
            num_of_digits += 1
    
    # 3) If the number of digits is more than 3, return 'No'
    if num_of_digits > 3:
        return 'No'
    
    # 4) Split the string by dot
    file_name_list = file_name.split('.')
    
    # 5) If the number of list items is not equal to 2, return 'No'
    if len(file_name_list) != 2:
        return 'No'
    
    # 6) If the first element of the list is empty, return 'No'
    if len(file_name_list[0]) < 1:
        return 'No'
    
    # 7) If the first element of the list doesn't start with a latin letter, return 'No'
    if (ord(file_name_list[0][0]) < 97) or (ord(file_name_list[0][0]) > 122):
        if (ord(file_name_list[0][0]) < 65) or (ord(file_name_list[0][0]) > 90):
            return 'No'
    
    # 8) If the second element of the list is not one of these ['txt', 'exe', 'dll'], return 'No'
    if file_name_list[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
