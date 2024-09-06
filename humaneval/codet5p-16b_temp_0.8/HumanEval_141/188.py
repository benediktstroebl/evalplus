
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

    dot_count = 0
    dot_substring_count = 0
    latin_alphapet = ['a', 'A', 'z', 'Z', 'a', 'A', 'Z', 'z']
    if len(file_name) >= 3 and len(file_name) <= 10:
        for char in file_name:
            if char in latin_alphapet:
                dot_substring_count += 1
                break
            elif char == '.':
                dot_count += 1
        if dot_count == 1 and dot_substring_count == 1:
            if file_name[file_name.index('.') - 1]!= '':
                if file_name[file_name.index('.') + 1] in ['exe', 'dll', 'txt']:
                    return 'Yes'
    return 'No'
