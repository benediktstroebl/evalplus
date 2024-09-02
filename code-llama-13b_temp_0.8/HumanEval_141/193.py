
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
    counter = 0
    if len(file_name) == 0:
        return "No"

    for i in range(len(file_name)):
        if (ord(file_name[i]) >= 48 and ord(file_name[i]) <= 57):
            counter += 1

    if (counter > 3):
        return "No"

    if (file_name.find(".") == -1 or file_name.find(".") == 0 or file_name.find(".") == len(file_name) - 1):
        return "No"

    index = file_name.find(".")
    substringBefore = file_name[:index]
    substringAfter = file_name[index + 1:]

    if (ord(substringBefore[0]) < 65 or (ord(substringBefore[0]) > 90 and ord(substringBefore[0]) < 97) or ord(substringBefore[0]) > 122):
        return "No"

    if (substringAfter != "txt" and substringAfter != "exe" and substringAfter != "dll"):
        return "No"

    return "Yes"
