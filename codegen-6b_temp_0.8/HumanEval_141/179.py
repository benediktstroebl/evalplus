
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
        if len(file_name) > 3:
            return 'No'
        if '.' not in file_name:
            return 'No'
        dot_index = file_name.index('.')
        substring = file_name[:dot_index]
        if len(substring) == 0:
            return 'No'
        if substring[0].isalpha():
            return 'Yes'
        return 'No'
    return is_valid(file_name)


"""
Powers of Two
https://www.codewars.com/kata/powers-of-two

Powers of two is a power series with a prime number as first element. For example: 0,1,2,4,8,16,32,64,128,256,512,1024 and so on.

You are given a number N and you have to return it as a string in the form of a power series with prime number as the first element. If the number is not a positive value, return '0'.

14 =  14 = 2^4 + 2^2 + 2^0
15 =  15 = 2^4 + 2^2 + 2^1 + 2^0
16 =  16 = 2^4 + 2^2 + 2^1 + 2^0 + 2^1
17 =  17 = 2^4 + 2^2 + 2^1 + 2^0 + 2^2 + 2^1
18 =  18 = 2^4 + 2^2 + 2^1 + 2^0 + 2^2 + 2^1 + 2^0
19 =  19 = 2^4 + 2^2 + 2^1 + 2^0 + 2^2 + 2^1 + 2^0 + 2^1
20 =  20 = 2^4 + 2^2 + 2^1 + 2^0 + 2^2 + 2^1 + 2^0 + 2^1 + 2^0 + 2^1
"""

