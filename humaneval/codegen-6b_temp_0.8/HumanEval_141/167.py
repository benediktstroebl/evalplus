
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
    import re
    # Some example patterns:
    pattern_1 = re.compile(r"^([a-z]|[A-Z])*\..*$")
    pattern_2 = re.compile(r"^([a-z]|[A-Z])*\..*\.[a-z]*$")
    pattern_3 = re.compile(r"^([a-z]|[A-Z])*$")
    pattern_4 = re.compile(r"^[a-z]|[A-Z]([a-z]|[A-Z])*\.[a-z]*$")
    pattern_5 = re.compile(r"^[a-z]|[A-Z]([a-z]|[A-Z])*$")
    pattern_6 = re.compile(r"^[a-z]|[A-Z]$")
    pattern_7 = re.compile(r"^[a-z]|[A-Z][a-z]*$")
    pattern_8 = re.compile(r"^[a-z]{{1,3}}\.[a-z]*$")
    pattern_9 = re.compile(r"^[a-z]{{1,3}}$")
    pattern_10 = re.compile(r"^[a-z]$")
    pattern_11 = re.compile(r"^[a-z]$")
    pattern_12 = re.compile(r"^[a-z][a-z]+$")
    pattern_13 = re.compile(r"^[a-z][a-z]*$")
    pattern_14 = re.compile(r"^[a-z]{1,3}$")
    pattern_15 = re.compile(r"^[a-z]{1,3}[a-z]*$")
    pattern_16 = re.compile(r"^[a-z]{1,3}[a-z]{1,3}$")
    pattern_17 = re.compile(r"^[