
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
    # The file name check
    invalid_char = re.match(r'^[\w\s]+$', file_name)
    if invalid_char:
        return 'No'
    else:
        invalid_char = re.match(r'^[0-9]+$', file_name)
        if invalid_char:
            return 'No'
        else:
            invalid_char = re.search(r'^[a-zA-Z]+', file_name)
            if invalid_char:
                start = invalid_char.start(0)
                dot = invalid_char.end(0)
                end = len(file_name)
                for i in range(start, end):
                    if file_name[i] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                        return 'No'
            else:
                return 'No'
            
    return 'Yes'
