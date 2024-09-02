
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
    flag = 0
    count = 0
    after_dot = 0
    if "." in file_name:
        flag += 1
    if flag > 0:
        index = file_name.index(".")
        sub_string = file_name[0:index]
        if sub_string == "":
            flag += 1
        elif sub_string[0].isalpha() is False:
            flag += 1
        if flag == 0:
            sub_string2 = file_name[index + 1:]
            if sub_string2 == "txt" or sub_string2 == "exe" or sub_string2 == "dll":
                for i in file_name:
                    if i.isdigit():
                        count += 1
                    if count > 3:
                        flag += 1
                        break
    if flag == 0:
        return "Yes"
    else:
        return "No"
