
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
    # This function takes a file name as input, and checks whether it is valid or not
    # Here we will implement the logic that checks the file name is valid or not
    # The logic is given in the problem statement
    # We will use regular expression to match the file name pattern and check whether it is valid or not
    # For example, to check whether the name contains exactly one dot, we can use the pattern '(\.\w+)'
    # Here, \w is a regex pattern that matches a word character (alphanumeric character or '_'),
    # and \* is a special character that matches zero or more of the preceding character
    # So the pattern '(\.\w+)' matches a string that contains exactly one dot
    # We can use other regex patterns to match other conditions as well
    # For example, to check whether the name starts with a latin alphapet letter, we can use the pattern '^[a-zA-Z][a-zA-Z0-9]*$'
    # Here, the pattern '^' matches the start of the string, and the pattern '$' matches the end of the string
    # The character class '[a-zA-Z][a-zA-Z0-9]*' matches one or more letters from the latin alphabet ('a'-'z' and 'A'-'Z')
    # And the '*' is used to match zero or more of the preceding character
    # We can combine these patterns to check all the conditions and return 'Yes' if the file name is valid
    # and return 'No' otherwise

    # Here we are using the re module of python to check the file name pattern
    # Here, we are checking the file name pattern with the regular expression
    # Here we are using the re.match function to check the file name pattern
    # If the re.match returns a match object, it means that the file name pattern is valid
    # Otherwise, it means that the file name pattern is not valid
    # We are checking the re.match object with the file name pattern
    # If the re.match object is not None, it means that the file name pattern is valid
    # otherwise, it means that the file name pattern is not valid
    if re.match(r'^[a-zA-Z][a-zA-Z
