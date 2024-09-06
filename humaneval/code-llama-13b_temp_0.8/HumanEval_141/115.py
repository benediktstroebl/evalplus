
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
    """Question:
    If the name is valid, the function should return 'Yes'. Otherwise, it should return 'No'.
    (see below)
    IMPORTANT:
    You are not supposed to handle the cases when the input is not a string.
    Your function should be as short as possible.
    """
    return 'Yes' if ((len(list(filter(lambda x: x.isdigit(), file_name))) <= 3)
                     and ('.' in file_name)
                     and (file_name.count('.') == 1)
                     and (not file_name.startswith('.'))
                     and (file_name[file_name.index('.') + 1:].lower() in ['txt', 'exe', 'dll'])
                     ) else 'No'
    """Example solution:
    # line 1
    if not isinstance(file_name, str):
      return 'No'
    # line 2
    if len(file_name) > 15:
      return 'No'
    # line 3
    name, ext = file_name.split('.')
    # line 4
    if (len(name) == 0 or name[0].isdigit() or not name[0].isalpha() or len(ext) != 3 or ext not in ('txt', 'exe', 'dll')):
      return 'No'
    # line 5
    return 'Yes'
    """
    
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION
