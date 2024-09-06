
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
    # your code here
    str_array = list(file_name)
    if len(str_array) < 3:
        return 'No'
    if str_array.count('.') > 1:
        return 'No'
    #if str_array[0].isalpha() == False:
    #    return 'No'
    if str_array.count('.') == 1:
        if (str_array[len(str_array) - 3].isdigit() == True and str_array[len(str_array) - 2].isdigit() == True and str_array[len(str_array) - 1].isdigit() == True) or str_array[len(str_array) - 3].isalpha() == False or str_array[len(str_array) - 2].isalpha() == False or str_array[len(str_array) - 1].isalpha() == False:
            return 'No'
        if str_array[len(str_array) - 3].isdigit() == True or str_array[len(str_array) - 2].isdigit() == True or str_array[len(str_array) - 1].isdigit() == True:
            return 'No'
    if str_array.count('.') == 0:
        return 'No'
    if str_array[len(str_array) - 3] != '.':
        return 'No'
    if (str_array[len(str_array) - 3] == '.' and str_array[len(str_array) - 2].isdigit() == True) or (str_array[len(str_array) - 2] == '.' and str_array[len(str_array) - 1].isdigit() == True):
        return 'No'
    if str_array[len(str_array) - 3] == '.' and (str_array[len(str_array) - 2] == 't' and str_array[len(str_array) - 1] == 'x' and str_array[len(str_array) - 4] == 'e') or (str_array[
