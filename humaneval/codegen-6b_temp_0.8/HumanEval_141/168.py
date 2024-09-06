
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
    def file_name_check_helper(file_name):
        """
        Helper function, which returns 'Yes' if the file name is valid, and 'No' otherwise.
        """
        n_digits = 0
        has_dot = False
        is_exe = False
        is_dll = False
        if file_name[-4:] == '.txt':
            is_exe = True
        elif file_name[-4:] == '.dll':
            is_dll = True
        else:
            return 'No'
        for char in file_name:
            if char.isdigit():
                n_digits += 1
                continue
            if char == '.':
                has_dot = True
                break
            if char not in string.ascii_letters:
                return 'No'
        if n_digits > 3:
            return 'No'
        if not has_dot:
            return 'No'
        if is_exe:
            if file_name[0] not in string.ascii_letters:
                return 'No'
            if file_name[-3:] not in ['exe', 'dll']:
                return 'No'
        if is_dll:
            if file_name[-3:] != 'dll':
                return 'No'
        return 'Yes'
    return file_name_check_helper

