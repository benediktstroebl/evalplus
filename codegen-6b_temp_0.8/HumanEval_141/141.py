
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
    def yes_no(file_name):
        #count .
        count = 0
        for i in file_name:
            if i == ".":
                count += 1
        #check that there is only one .
        if count != 1:
            return "No"
        #check that the substring is not empty
        for i in range(len(file_name)):
            if file_name[i] == ".":
                break
            #check that the substring is not empty
            if file_name[i] == "":
                return "No"
            #check that the substring is not empty
            if (i+1) == len(file_name):
                return "No"
            #check that the substring is not empty
            if file_name[i+1] == " ":
                return "No"
            #check if the substring starts with a latin letter
            if file_name[i].isalpha() and file_name[i+1].isalpha():
                #check that the substring after the . is one of these: ['txt', 'exe', 'dll']
                if (file_name[i+1] == "t" or file_name[i+1] == "e" or file_name[i+1] == "x" or file_name[i+1] == "d"):
                    return 'Yes'
        return "No"
    if file_name == "":
        return "No"
    #check that there is not more than three digits ('0'-'9') in the file's name.
    for i in file_name:
        if i.isdigit():
            return "No"
    #check that the file's name contains exactly one dot '.'
    if file_name.find(".") == -1:
        return "No"
    #check that the substring before the . is not empty, and it is not a symbol
    for i in range(len(file_name)):
        if file_name[i] == ".":
            break
        if file_name[i] == " ":
            return "No"
        if file_name[i] == "0" or