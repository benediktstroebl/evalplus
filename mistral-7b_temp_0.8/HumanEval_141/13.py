
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
    count = 0
    for i in range(len(file_name)):
        if file_name[i] == ".":
            count += 1

    count1 = 0
    for i in range(len(file_name)):
        if file_name[i].isalpha():
            count1 += 1
        elif file_name[i].isdigit():
            count1 += 1
            count += 1

    count2 = 0
    for i in range(len(file_name)):
        if file_name[i] == ".":
            count2 += 1

    if count == 1 and count1 > 0 and count2 == 1:
        if file_name[-3:] in ["txt", "exe", "dll"]:
            return "Yes"
        else:
            return "No"
    else:
        return "No"









































