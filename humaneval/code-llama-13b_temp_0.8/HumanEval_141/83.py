
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
    if len(file_name) <= 1:
        return "No"
    elif file_name[0] < "a" or file_name[0] > "z":
        return "No"
    else:
        dot = 0
        letter = 0
        digit = 0
        i = 0
        while i < len(file_name):
            if file_name[i] == ".":
                dot += 1
            elif file_name[i] >= "a" and file_name[i] <= "z":
                letter += 1
            elif file_name[i] >= "A" and file_name[i] <= "Z":
                letter += 1
            elif file_name[i] >= "0" and file_name[i] <= "9":
                digit += 1
            if dot > 1 or letter < 1 or digit > 3:
                return "No"
            i += 1
        if dot == 1 and letter >= 1 and digit <= 3:
            return "Yes"
        else:
            return "No"
