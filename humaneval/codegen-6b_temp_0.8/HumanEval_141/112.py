
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
    
    def checkChar(string):
        ascii_val = ord(string)
        if 65 <= ascii_val <= 90 or 97 <= ascii_val <= 122:
            return True
        elif ascii_val == 46:
            return True
        else:
            return False
        
    def check_file_name(file_name):
        count = 0
        if len(file_name) <= 3:
            return "No"
        elif file_name[0] in string.ascii_lowercase:
            count += 1
        if file_name[-1] != "." or file_name[-2] != ".":
            return "No"
        elif file_name[1] not in string.ascii_lowercase:
            return "No"
        elif file_name[2] == ".":
            if file_name[-3:] in ["txt", "exe", "dll"]:
                count += 1
            else:
                return "No"
        else:
            while file_name[-3] in string.ascii_lowercase:
                if checkChar(file_name[-3]):
                    count += 1
                else:
                    return "No"
                file_name = file_name[:-1]
            return "Yes" if count == 2 else "No"
    return check_file_name(file_name)
