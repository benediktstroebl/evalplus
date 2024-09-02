
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
    #Write your code here
    a = "1example.dll"
    b = "1example.txt"
    c = "1example.exe"
    d = "example.txt"
    e = "example.exe"
    f = "example.dll"
    g = "1a.txt"
    h = "1a.dll"
    i = "1a.exe"
    j = "a.txt"
    k = "a.dll"
    l = "a.exe"
    m = "12.txt"
    n = "12.dll"
    o = "12.exe"
    p = "123.txt"
    q = "123.dll"
    r = "123.exe"
    s = "example1.txt"
    t = "example1.dll"
    u = "example1.exe"
    v = "1example.txt"
    w = "1example.dll"
    x = "1example.
