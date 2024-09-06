
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
    def check_file_name(name):
        # check 1st condition
        if not name.isdigit():
            if name.find('.') != -1:
                if name[0].isalpha() and name[0].isalpha():
                    if name[0].lower() == 'a':
                        # check 2nd condition
                        if len(name) == 10:
                            if name.find('exe') != -1 or name.find('dll') != -1:
                                return 'Yes'
                            else:
                                return 'No'
                        else:
                            return 'No'
                    else:
                        return 'No'
                else:
                    return 'No'
            else:
                return 'No'
        else:
            return 'No'

    return check_file_name(file_name)

