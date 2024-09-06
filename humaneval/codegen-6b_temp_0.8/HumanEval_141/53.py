
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
        valid = re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.[a-zA-Z0-9]+$', file_name)
        if valid:
            valid = re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', file_name)
            if valid:
                regex = re.compile(r'\.[a-zA-Z0-9]+$')
                valid = not regex.match(file_name)
                if valid:
                    valid = re.match(r'^[a-zA-Z]+$', file_name)
                    if valid:
                        return 'Yes'
                    else:
                        return 'No'
                else:
                    return 'No'
            else:
                return 'No'
        else:
            return 'No'
    return is_valid(file_name)


"""
Task 5.
Write a function which takes a string as an argument and calculates the number of 
consecutive vowels in the string. For example:

(str, result) = "hello world", 2 
(str, result) = "aabbccdd", 2 
(str, result) = "", 0 
(str, result) = "abracadabra", 5 
(str, result) = "abcdabcdabcdabcd", 5 
(str, result) = "this is a test", 1 
(str, result) = "testing is important", 2
"""

