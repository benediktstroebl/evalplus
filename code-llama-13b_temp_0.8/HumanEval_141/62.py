
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
    # Your code here
    if len(file_name.split(".")[0]) == 0 or len(file_name.split(".")[1]) == 0:
        return "No"
    if file_name.count(".") > 1 or len(file_name.split(".")[1]) not in (3,4):
        return "No"
    if file_name.count(".") == 0 or file_name.count(".") == 1:
        return "No"
    if file_name.split(".")[1] not in ("txt","exe","dll"):
        return "No"
    if file_name.split(".")[1] in ("exe","dll") and file_name.count(".") == 2 and file_name.count(".") == 2 and file_name.count(".") != 2:
        return "No"
    if file_name.split(".")[1] in ("txt","exe","dll") and file_name.count(".") == 2 and file_name.count(".") == 2 and file_name.count(".") == 2:
        return "No"
    if file_name.split(".")[0].isalpha() == False:
        return "No"
    if file_name.split(".")[0][0].isalpha() == False:
        return "No"
    if file_name.count(".") == 2 and file_name.split(".")[0][0].isalpha() == False:
        return "No"
    if file_name.count(".") == 3 and file_name.split(".")[0][0].isalpha() == False:
        return "No"
    for letter in file_name.split(".")[1]:
        if ord(letter) not in range(48,57) and ord(letter) not in range(65,90) and ord(letter) not in range(97,122):
            return "No"
    if file_name.split(".")[1].isalpha() == True:
        return "No"
    if file_name.split(".")[0].isdigit() == True:
        return "No"
