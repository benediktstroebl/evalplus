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
    if len(files[0]) == 0 or not files[0][0].isalpha():
        return "No"
    if len(files[1]) != 4 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    numbers = sum(1 for c in files[0] if c.isdigit())
    if numbers > 3:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes a string `file_name` as input and returns either 'Yes' or 'No' depending on if the filename conforms to the specified rules or not. The rules are:
- It should not have more than three consecutive digits.
- It should have exactly one dot '.'.
- The part before the dot should start with a letter and not be empty.
- The part after the dot should be either 'txt', 'exe', or 'dll'.

The function checks for these conditions and returns 'Yes' if the file name is valid and 'No' otherwise. You can use this function to validate file names according to the specified rules.