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
    files = file_name.split('.')
    if len(files) != 2:
        return "No"
    if len(files[0]) == 0 or not files[0][0].isalpha():
        return "No"
    if len(files[1]) != 3 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    no_digits = sum(1 for char in files[0] if char.isdigit())
    if no_digits > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a string representing a file's name as input. This function returns `'Yes'` if the given file name is valid, and `'No'` otherwise. This function defines the validity of the file name based on the following conditions:
1. The file name should not contain more than three digits ('0'-'9').
2. The file name contains exactly one dot '.' character.
3. The substring before the dot should not be empty and should start with a letter from the Latin alphabet ('a'-'z' or 'A'-'Z').
4. The substring after the dot should be one of the following: ['txt', 'exe', 'dll'].

The function checks each condition and returns the appropriate response ('Yes' or 'No') based on the evaluation of the conditions. You can use this function to validate file names based on the provided criteria.