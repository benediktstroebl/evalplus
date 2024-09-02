
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
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    if digits.count(file_name[0]) == 0 and digits.count(file_name[1]) == 0 and 
       digits.count(file_name[2]) == 0 and digits.count(file_name[3]) == 0 and 
       digits.count(file_name[4]) == 0 and digits.count(file_name[5]) == 0 and 
       digits.count(file_name[6]) == 0 and digits.count(file_name[7]) == 0 and 
       digits
