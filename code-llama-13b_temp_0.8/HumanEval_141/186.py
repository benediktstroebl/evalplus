
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
    counter = 0
    counter2 = 0
    counter3 = 0
    if len(file_name) > 1:
        for i in range(len(file_name)):
            if file_name[i] >= '0' and file_name[i] <= '9':
                counter += 1
        if counter >= 3:
            counter2 = 1
    else:
        counter2 = 1
    if counter2 != 1:
        for i in range(len(file_name)):
            if file_name[i] >= 'a' and file_name[i] <= 'z':
                counter3 = 1
                break
            elif file_name[i] >= 'A' and file_name[i] <= 'Z':
                counter3 = 1
                break
        if counter3 != 1:
            counter2 = 1
        else:
            counter2 = 0
    else:
        counter2 = 1
    if file_name[-1] != '.':
        counter2 = 1
    else:
        counter2 = 0
    if counter2 != 1:
        for i in range(len(file_name)):
            if file_name[i] == '.':
                if file_name[i + 1: i + 4] == 'txt' or file_name[i + 1: i + 4] == 'exe' or file_name[i + 1: i + 4] == 'dll':
                    counter2 = 0
                    break
                else:
                    counter2 = 1
                    break
    if counter2 == 1:
        return 'No'
    else:
        return 'Yes'





