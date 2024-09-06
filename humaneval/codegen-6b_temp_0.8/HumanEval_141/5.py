
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
    def valid_input(*args):
        _file_name = file_name
        if _file_name == None:
            raise ValueError("No filename provided")
        if not isinstance(_file_name, str):
            raise ValueError("Argument is not a string")
        if len(_file_name) == 0:
            raise ValueError("filename is empty")
        if not _file_name[0].isalpha():
            raise ValueError("filename should start with a letter")
        # check there is only one dot '.'
        if '.' in _file_name:
            index = _file_name.index(".")
            if index < len(_file_name) - 3:
                raise ValueError("filename should contain at least a three letter substring after the dot")
            if len(_file_name) - index < 4:
                raise ValueError("filename should contain at least a four letter substring after the dot")
            if not _file_name[index+3:].isalpha():
                raise ValueError("filename should contain a letter after the dot")
            if not _file_name[index+4:].lower() in ['txt', 'exe', 'dll']:
                raise ValueError("filename should contain txt, exe or dll after the dot")
        else:
            raise ValueError("filename should contain a dot")
        return
    return valid_input
