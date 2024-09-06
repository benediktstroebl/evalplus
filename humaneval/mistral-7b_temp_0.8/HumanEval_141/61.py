
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


    def check_first_sub(file_name):
        """
        Check if substring before the dot is empty or starts with a letter from latin alphapet
        """
        if file_name[0] == ".":
            return False
        try:
            return file_name[0].lower() in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        except IndexError:
            return False

    def check_second_sub(file_name):
        """
        Check if substring after the dot is in ['txt', 'exe', 'dll']
        """
        try:
            return file_name[file_name.index(".")+1:].lower() in "txt exe dll"
        except ValueError:
            return False

    def check_digits(file_name):
        """
        Check if there are more than three digits
        """
        if file_name[0] in "0123456789":
            return False
