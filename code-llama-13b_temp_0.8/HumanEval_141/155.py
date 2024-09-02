
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

    #code here
    digit_count = 0
    if not "." in file_name:
      return "No"
    sub_str1, sub_str2 = file_name.split(".")
    if not sub_str1 or not sub_str2:
      return "No"
    if sub_str2 not in ("txt", "exe", "dll"):
      return "No"
    if not sub_str1[0].isalpha():
      return "No"
    for i in sub_str1:
      if i.isdigit():
        digit_count += 1
    if digit_count > 3:
      return "No"
    return "Yes"
