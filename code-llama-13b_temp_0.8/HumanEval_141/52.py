
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
    # An empty list to store the results.
    results = []
    # To count the number of digits ('0'-'9') in the file's name.
    count = 0
    # To store the result for each condition.
    result = 0
    # The index of the dot.
    dot_index = 0
    # The substring before the dot.
    before_dot = ''
    # The substring after the dot.
    after_dot = ''
    # Loop over the characters in the string.
    for index, char in enumerate(file_name):
        # Increase the number of digits.
        if char >= '0' and char <= '9':
            count += 1
        # Check if the dot is present in the string.
        if char == '.':
            # If the dot was already found, then it's not a valid name.
            if dot_index:
                return 'No'
            # The index of the dot.
            dot_index = index
            # The substring before the dot.
            before_dot = file_name[ : dot_index]
            # The substring after the dot.
            after_dot = file_name[dot_index + 1 : ]
        # Check if the string is valid.
        if index == 0:
            if char < 'a' or char > 'z':
                result = 0
        # Check if the first character is a letter.
        if index == 0 and not (char >= 'a' and char <= 'z'):
            result = 0
        # Check if there are not more than three digits.
        if count > 3:
            result = 0
        # Check if the string is equal to the substring before the dot.
        if file_name[:dot_index] != before_dot:
            result = 0
        # Check if the file's name is equal to the substring after the dot.
        if file_name[dot_index + 1 :] != after_dot:
            result = 0
        # Check if the file's name contains the substring after the dot.
        if file_name[dot_index + 1 :] not in ['.txt', '.exe', '.
