
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
    file_name = file_name.lower()
    with open(file_name) as f:  # access the file
        content = f.read()
        result = True
        if not content:
            result = False
        
        if len(content) > 3 and not content.isdigit():
            result = False
        
        if '.' not in file_name and content != "\n":
            result = False
        
        if len(content) > 0:
            if content[0].isalpha() and content[0].isupper():
                if content[-4:] not in ['txt', 'dll', 'exe']:
                    result = False
            else:
                result = False
    return 'Yes' if result else 'No'


assert file_name_check("example.txt") == 'Yes'
assert file_name_check("1example.dll") == 'No'
assert file_name_check("example.exe") == 'Yes'
assert file_name_check("1example.txt") == 'No'
assert file_name_check("1example.exe") == 'Yes'
assert file_name_check("1example.dll") == 'No'
assert file_name_check("example") == 'No'
assert file_name_check("ex") == 'No'
assert file_name_check("EXAMPLE") == 'Yes'
assert file_name_check("EXAMPLE.") == 'Yes'
assert file_name_check("EXAMPLE.txt") == 'Yes'
assert file_name_check("EXAMPLE.exe") == 'Yes'
assert file_name_check("EXAMPLE.dll") == 'No'
assert file_name_check("EXAMPLE.DS_Store") == 'No'
assert file_name_check("EXAMPLE.dwg") == 'No'
assert file_name_check("EXAMPLE.txt.gz") == 'Yes'
assert file_name_check("EXAMPLE.tgz") == 'No'
assert file_name_check("EXAMPLE.gz") == 'Yes'
assert file_name_check("EXAMPLE.tar.gz") == 'No'
assert file_name