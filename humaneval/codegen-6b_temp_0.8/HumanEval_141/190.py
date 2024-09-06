
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
    def check_name(name):
        o = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        is_alpha_letter = is_latin_alphabet(name)
        if name=='.' or is_alpha_letter==False:
            return 'No'
        elif name[0]=='.' and is_alpha_letter==True:
            return 'Yes'
        elif len(name)<=3:
            return 'No'
        elif name[3]=='.' and is_alpha_letter==True:
            return 'Yes'
        elif len(name)<=3:
            return 'No'
        elif name[-4:] not in ['txt', 'exe', 'dll']:
            return 'No'
        elif name[3]=='.':
            return 'Yes'
            
    return check_name(file_name)
    