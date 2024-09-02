
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
    if len(file_name) >= 4:
        return "No"
    else:
        a = 0
        for i in file_name:
            if i.isdigit():
                a += 1
        if a > 3:
            return "No"
        else:
            if len(file_name) > 3:
                if file_name[0].isalpha() == False:
                    return "No"
                else:
                    if file_name[3] != ".":
                        return "No"
                    else:
                        if len(file_name) < 3:
                            return "No"
                        else:
                            if file_name[4] == "t" and file_name[5] == "x" and file_name[6] == "t":
                                return "Yes"
                            elif file_name[4] == "e" and file_name[5] == "x" and file_name[6] == "e":
                                return "Yes"
                            elif file_name[4] == "d" and file_name[5] == "l" and file_name[6] == "l":
                                return "Yes"
                            else:
                                return "No"
            else:
                if file_name[0].isalpha() == False:
                    return "No"
                else:
                    if file_name[1] == "." and file_name[2] == "t" and file_name[3] == "x" and file_name[4] == "t":
                        return "Yes"
                    elif file_name[1] == "." and file_name[2] == "e" and file_name[3] == "x" and file_name[4] == "e":
                        return "Yes"
                    elif file_name[1] == "." and file_name[2] == "d" and file_name[3] == "l" and file_name[4] == "l":
                        return "Yes"
                    else:
                        return "No"
                
    
