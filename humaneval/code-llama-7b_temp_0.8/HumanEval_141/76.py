
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
    return file_name.count(".")==1 and file_name.count("0")<=2 and file_name.count("1")<=2 and file_name.count("2")<=2 and file_name.count("3")<=2 and file_name.count("4")<=2 and file_name.count("5")<=2 and file_name.count("6")<=2 and file_name.count("7")<=2 and file_name.count("8")<=2 and file_name.count("9")<=2 and file_name.count(".")==1 and file_name.startswith("0")==False and file_name.startswith("1")==False and file_name.startswith("2")==False and file_name.startswith("3")==False and file_name.startswith("4")==False and file_name.startswith("5")==False and file_name.startswith("6")==False and file_name.startswith("7")==False and file_name.startswith("8")==False and file_name.startswith("9")==False and file_name[0].islower()==True and file_name[0].isupper()==True and (file_name[1]=='.' and file_name[2:4]=="txt" or file_name[1]=='.' and file_name[2:4]=="exe" or file_name[1]=='.' and file_name[2:4]=="dll") 

