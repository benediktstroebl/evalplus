
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
    #split the string into the substring before the dot and the substring after the dot
    str_split = file_name.split(".")
    #print(str_split)
    #check to make sure there are no more than three digits in the name
    if len([char for char in file_name if char.isdigit()]) > 3:
        return "No"
    #check to make sure there is exactly one dot in the string
    elif len(str_split)!= 2:
        return "No"
    #check to make sure there is text before the dot, and that the first character is a letter
    elif not str_split[0] or not str_split[0][0].isalpha():
        return "No"
    #check to make sure the second substring after the dot is one of the values in the list
    elif str_split[1] not in ['txt', 'exe', 'dll']:
        return "No"
    #if all conditions are met, return "Yes"
    else:
        return "Yes"
