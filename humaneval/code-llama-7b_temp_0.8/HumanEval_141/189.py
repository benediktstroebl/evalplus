
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
    # please note that file_name is a string not a list
    # so we convert it to a list in order to iterate
    file_name_to_list = list(file_name)

    if file_name.count('.') > 1:
        return "No"

    # so we check if the 1st and the last symbols are of latin alphabet
    # we do this to check if the first letter is an alphabet letter
    if (file_name_to_list[0] >= 'a' and file_name_to_list[0] <= 'z') or (file_name_to_list[0] >= 'A' and file_name_to_list[0] <= 'Z'):
        if (file_name_to_list[-1] >= 'a' and file_name_to_list[-1] <= 'z') or (file_name_to_list[-1] >= 'A' and file_name_to_list[-1] <= 'Z'):
            pass
        else:
            return "No"
    else:
        return "No"

    # so now we check for the numbers in the string
    for i in range(len(file_name_to_list)):
        if file_name_to_list[i] >= '0' and file_name_to_list[i] <= '9':
            if i > 2:
                return "No"

    # so now we check if there is an alphabet letter before the dot
    # and if the letters after the dot are valid
    if file_name_to_list.index('.') > 0:
        if (file_name_to_list[0] >= 'a' and file_name_to_list[0] <= 'z') or (file_name_to_list[0] >= 'A' and file_name_to_list[0] <= 'Z'):
            pass
        else:
            return "No"

    # now check the letters after the dot
    if file_name_to_list[-1] == '.':
        return "No"
    elif file_name_to_list[-1] == 't':
        if file_name_to_
