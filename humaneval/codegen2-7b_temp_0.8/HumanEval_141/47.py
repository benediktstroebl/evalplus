
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
    def valid_file_name(filename):
        if re.match(r'^[0-9]{3,}$', filename) is None:
            return 'No'
        if filename.count('.')!= 1:
            return 'No'
        extension = filename.split('.')[-1]
        if extension not in ['txt', 'exe', 'dll']:
            return 'No'
        if re.match(r'^[a-zA-Z]', filename.split('.')[0]) is None:
            return 'No'
        return 'Yes'
    return valid_file_name(file_name)
