
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
    # Initialize the result variable
    result = "No"
    
    # Split the file name into its substrings
    file_name_list = file_name.split(".")
    
    # Check if the file name starts with a digit
    if len(file_name_list[0]) > 1:
        result = "No"
        return result
    
    # Check if the file name contains only one dot
    if len(file_name_list) != 2:
        result = "No"
        return result
    
    # Check if the file name starts with a letter
    if not file_name_list[0].isalpha():
        result = "No"
        return result
    
    # Check if the file name ends with one of the allowed extensions
    allowed_extensions = ["txt", "exe", "dll"]
    if not allowed_extensions.count(file_name_list[1]):
        result = "No"
        return result
    
    # If all conditions are met, the result should be 'Yes'
    return "Yes"
