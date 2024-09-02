
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
    # Please use the name of the parameter to represent the variable that stores the file name

    # Please use the following conditions to check if the file name is valid or not
    # 1. there should not be more than three digits ('0'-'9') in the file's name
    # 2. the file's name contains exactly one dot '.'
    # 3. the substring before the dot should not be empty, and it starts with a letter from 
    # the latin alphapet ('a'-'z' and 'A'-'Z').
    # 4. the substring after the dot should be one of these: ['txt', 'exe', 'dll']

    # You can only use the following conditions and methods on strings and lists
    # string methods: isdigit(), isalnum(), isalpha(), startswith(), count()
    # list methods: count()
    return ''
