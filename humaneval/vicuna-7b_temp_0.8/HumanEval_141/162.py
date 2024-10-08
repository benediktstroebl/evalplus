
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
    def check(file_name):
        # check for more than three digits
        if len(file_name) > 3:
            return 'No'
        # check if the name contains exactly one dot
        if '.' not in file_name:
            return 'No'
        # check if the substring before the dot is empty or starts with a latin alphapet letter
        if not file_name.startswith(chr(ord('a')+i) for i in range(ord('a'), ord('z')+1)) or len(file_name.split(".")[0]) == 0:
            return 'No'
        # check if the substring after the dot is one of the allowed extensions
        if file_name.split(".")[1].lower() not in ['txt', 'exe', 'dll']:
            return 'No'
        return 'Yes'
    return check(file_name)
