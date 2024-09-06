
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
    # **********
    # 1. Remove all digits from the file's name
    # **********
    #file_name = re.sub(r'\d', '', file_name)
    # **********
    # 2. Check that the file's name contains only one dot
    # **********
    if file_name.count('.') != 1:
        return "No"

    # **********
    # 3. Check that the substring before the dot is not empty
    # **********
    substring = file_name.split('.')
    if substring[0] == '':
        return "No"

    # **********
    # 4. Check that the substring contains letters only
    # **********
    #if re.search(r'\D', substring[0]):
    #    return "No"
    # **********
    # 5. Check that the substring after the dot is one of these: ['txt', 'exe', 'dll']
    # **********
    if substring[1] not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"

