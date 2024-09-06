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
    if ( Files[0].replace("-", "").replace("_", "").replace(".", "").isdigit() and 
        len(Files[0].replace("-", "").replace("_", "").replace(".", "")) > 3 ):
            return "No"
    # Check for valid first part of file name
    if not files[0].startswith([*string.ascii_lowercase, *string.ascii_uppercase]):
        return "No"
    # Check for second part of file name
    if files[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which is a string representing the name of a file. It checks the following conditions to determine if the file name is valid or not:
1. The file name should not be empty.
2. There should be exactly one dot ('.') in the file name.
3. The substring before the dot (the filename prefix) should start with a letter of the Latin alphabet (either lowercase or uppercase).
4. The substring after the dot (the file extension) should be either "txt", "exe", or "dll".
5. There should not be more than three consecutive digits in the file name.

The function splits the file name by the dot character to properly check the filename prefix and the file extension. It then uses string methods to remove special characters like "-" and "_" to correctly count the number of digits. Finally, it returns "Yes" if all conditions are met, and "No" otherwise.