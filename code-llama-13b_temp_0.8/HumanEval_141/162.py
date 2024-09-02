
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
    #your code here
    # check for length
    digits = 0
    count = 0
    for i in range(len(file_name)):
      if file_name[i] >= '0' and file_name[i] <= '9':
        digits += 1
      if file_name[i] == '.':
        count += 1
    if len(file_name) == 0 or digits > 3 or count != 1:
      return 'No'
    
    # check for first character
    if file_name[0] < 'a' or (file_name[0] > 'z' and file_name[0] < 'A') or (file_name[0] > 'Z'):
      return 'No'

    # check for substring
    if file_name[-4:] != '.txt' and file_name[-4:] != '.exe' and file_name[-4:] != '.dll':
      return 'No'

    return 'Yes'

