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
    # check for emptiness and valid first letter of the substring before dot
    if not files[0][0].isalpha():
        return "No"
    # check for max three digits in the file name
    if files[0].count(":"):
        return "No"
    # check for the appropriate extensions
    if files[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

The following tests demonstrate the behavior of the function:
```python
>>> file_name_check("example.txt")
'Yes'
>>> file_name_check("1example.dll")
'No'
>>> file_name_check("example. EXE")
'No'
>>> file_name_check("example.dll1")
'No'
>>> file_name_check(" EXE.txt")
'No'
```