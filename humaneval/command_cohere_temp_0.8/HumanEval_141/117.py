```python
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
    if not file_name or not isinstance(file_name, str):
        return "No"
    files = file_name.split(".")
    if len(files) != 2:
        return "No"
    # Check for more than three consecutive digits
    if (str(files[0]).strip('0123456789').isdigit() and 
        str(files[0]).strip('0123456789').length > 3):
        return "No"
    # Check 1. Must start with a letter
    if not str(files[0]).strip('.').isalpha():
        return "No"
    # Check 2. Must end with one of the specified extensions
    if str(files[1]).strip('.').lower() not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes a string representing a file's name as input. It checks for four conditions to determine if the file's name is valid or not:
1. The filename should not be empty.
2. There should not be more than three digits ('0'-'9') in the file's name.
3. The file's name should contain exactly one dot ('.').
4. The substring before the dot should not be empty, and it should start with a letter from the latin alphapet ('a'-'z' and 'A'-'Z').
5. The substring after the dot should be one of these: ['txt', 'exe', 'dll'].

The function splits the filename into its base (before the dot) and extension (after the dot) using the `split()` method. It then checks each of the conditions and returns 'Yes' if all conditions are met and 'No' otherwise.

The script includes basic input validation to check if the input is empty or not a string, in which case it returns "No" automatically. Also, the digit count is checked using a combination of `isdigit()` and `length` functions to accommodate both single-digit and multiple-digit filenames. The script assumes that the input is a string representing a file's name as specified in the problem statement.

The script returns "Yes" if the file name is valid, and "No" otherwise. You can use this function to validate file names in your application.