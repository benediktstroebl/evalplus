
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
    # Your code here
    # check for three or more digits
    if len(re.findall(r'\d',file_name)) > 3:
        return "No"
    # check for the number of periods
    if len(re.findall(r'\.',file_name)) != 1:
        return "No"
    # check if the first char of the string is a letter
    if not re.search('[a-zA-Z]', file_name[0]):
        return "No"
    # check if the last three chars are txt, exe or dll
    if file_name[-3:] not in ['txt','exe','dll']:
        return "No"
    # check if the last char is a dot
    if file_name[-1] != '.':
        return "No"
    return "Yes"
    
