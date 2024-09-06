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
    if not file_name.startswith(tuple('abcDEFghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        return "No"
    file_name = file_name.replace('.', '')
    if len(file_name) > 3 and len(file_name) != 0:
        return "No"
    if len(file_name.split('.')) != 2:
        return "No"
    ext = file_name.split('.')[-1].lower()
    if ext not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which is a string that represents the name of a file. The function returns "Yes" if the specified file name is valid and meets all the criteria specified in the problem statement, and it returns "No" otherwise. 

The function evaluates boolean conditions and returns the corresponding answer ("Yes" or "No"). You can use it to quickly check if a file name is valid or not, as per the conditions provided.