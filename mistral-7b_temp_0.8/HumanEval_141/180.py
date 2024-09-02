
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

    # Write your code here.
    l = []
    l1 = []
    l2 = []
    l3 = []
    # l.append('abc.txt')
    # l.append('abc.dll')
    # l.append('abc.exe')
    # l.append('abc.exe')
    # l.append('abc123.txt')
    # l.append('abc123.dll')
    # l.append('abc123.exe')
    # l.append('123abc.txt')
    # l.append('123abc.dll')
    # l.append('123abc.exe')
    # l.append('123abc123.txt')
    # l.append('123abc123.dll')
    # l.append('123abc123.exe')
    # l.append('abc123.txt')
    # l.append('abc123.dll')
    # l.append('abc
