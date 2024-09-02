
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
    is_valid = "Yes"
    char_list = list(file_name)
    # Checks whether the file name starts with a letter
    if char_list[0].isalpha() == False:
        return "No"

    # Checks whether the file name ends with txt, exe or dll
    if not char_list[-3] == '.' or not char_list[-2:] in ['txt','exe','dll']:
        return "No"

    # Checks whether there is only one dot
    if len(list(filter(lambda x: x == '.', char_list))) != 1:
        return "No"

    # Checks whether there are no more than 3 digits
    if len(list(filter(lambda x: x.isdigit(), char_list))) > 3:
        return "No"
    
    return is_valid
