
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
    # return 'Yes' if the file name is valid, 'No' otherwise.
    counter = 0
    flag = 0
    if file_name.count('.') == 1:
        for i in range(len(file_name)):
            if file_name[i] == '.':
                if file_name[0] == '.' or file_name[-1] == '.':
                    flag = 1
                if flag == 0:
                    if file_name[0].isalpha():
                        if file_name[i + 1:].isalnum() and file_name[i + 1:].find('.') == -1:
                            break
                        else:
                            flag = 1
                    else:
                        flag = 1
                else:
                    flag = 1

        for i in range(len(file_name)):
            if file_name[i].isdigit():
                counter += 1
            if counter == 3:
                flag = 1
                break
    else:
        flag = 1
    if flag == 0:
        return 'Yes'
    else:
        return 'No'

