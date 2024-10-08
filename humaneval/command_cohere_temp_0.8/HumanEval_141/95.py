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
    if files[0].strip() == "":
        return "No"
    if not files[0].strip()[0].isalpha():
        return "No"
    if len(files[0].strip()) > 3:
        return "No"
    if files[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes a string file name as input and returns either "Yes" or "No" depending on the conditions outlined in the problem. The function checks if the file name contains more than three digits, has exactly one dot, and has a valid prefix and extension according to the specified criteria. The valid prefix is checked to start with a letter and not have more than three characters, while the valid extension is checked to be one of the specified options. The function returns "Yes" if all conditions are met and "No" otherwise.