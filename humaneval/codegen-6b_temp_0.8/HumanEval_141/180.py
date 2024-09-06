
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
    def valid_name(file_name):
        # Check the file name for validities
        if file_name[0].isdigit():
            return 'NO'
        if file_name.count('.') != 1:
            return 'NO'
        if file_name.split('.')[0] == '':
            return 'NO'
        for i, c in enumerate(file_name.split('.')[0]):
            if not c.isalpha() and c != "_":
                return 'NO'
        if file_name.split('.')[1] not in ["txt", "exe", "dll"]:
            return "NO"
        return "YES"
        #

    #
    # Please do not modify the code below this line
    #
    pred = r"^[a-zA-Z][a-zA-Z0-9_.]+$"
    return valid_name(file_name)
