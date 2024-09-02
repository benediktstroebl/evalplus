
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
    def is_valid(file_name):
        file_name = file_name.lower()
        if file_name.find('.') == -1 or file_name[0].isalpha() != True:
                return False
        dot_index = file_name.find('.')
        #check length
        if len(file_name) <= dot_index:
            return False
        #check only letters
        if not file_name[dot_index+1:].isalpha():
            return False
        #check three letters
        if len(file_name.split('.')[1]) != 3:
            return False
        #check exe, txt, dll
        if file_name.split('.')[1] not in ['exe', 'txt', 'dll']:
            return False
        #if everything was ok, return True
        return True
    return is_valid(file_name)
