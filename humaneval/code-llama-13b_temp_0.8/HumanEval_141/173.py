
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
    # case 1
    if file_name.count('.') == 1 and file_name.count('.') != len(file_name):
        # case 1.1
        if file_name[0].isalpha():
            # case 1.1.1
            if file_name[-4:] in ['txt', 'exe', 'dll']:
                # case 1.1.1.1
                if file_name[:-4].count('0') <= 3:
                    # case 1.1.1.1.1
                    if file_name[:-4].count('1') <= 3:
                        # case 1.1.1.1.1.1
                        if file_name[:-4].count('2') <= 3:
                            # case 1.1.1.1.1.1.1
                            if file_name[:-4].count('3') <= 3:
                                # case 1.1.1.1.1.1.1.1
                                if file_name[:-4].count('4') <= 3:
                                    # case 1.1.1.1.1.1.1.1.1
                                    if file_name[:-4].count('5') <= 3:
                                        # case 1.1.1.1.1.1.1.1.1.1
                                        if file_name[:-4].count('6') <= 3:
                                            # case 1.1.1.1.1.1.1.1.1.1.1
                                            if file_name[:-4].count('7') <= 3:
                                                # case 1.1.1.1.1.1.1.1.1.1.1.1
                                                if file_name[:-4].count('8') <= 3:
                                                    # case 1.1.1.1.1.1.1.1.1.1.1.1.1
                                                    if file_name[:-4].count('9') <= 3:
                                                        # case 1
