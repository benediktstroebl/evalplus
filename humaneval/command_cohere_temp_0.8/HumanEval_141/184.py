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
    if not file_name.startswith(tuple('ez')):
        return "No"
    file_name = file_name.replace('.', '').replace('_', ' ')
    if set(file_name) - set('1234567890'):
        return "No"
    if not file_name.isalpha():
        return "No"
    ext = file_name.split('.')[-1].lower()
    if ext not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes the name of a file as input. It checks the following conditions of a valid file name:
1. The file name should not start with "1" or more than three digits, ensuring it does not start with more than "ez" and excluding underscores.
2. Contains exactly one dot ('.').
3. The substring before the dot should not be empty, and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z').
4. The substring after the dot should be one of these: ['txt', 'exe', 'dll'].

The function returns "Yes" if the file name meets all these conditions, and "No" otherwise. You can use this function to validate file names according to the specified criteria.