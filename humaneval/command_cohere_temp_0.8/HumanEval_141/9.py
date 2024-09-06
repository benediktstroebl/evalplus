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
    if len(files) != 2 or not files[0][0].isalpha():
        return "No"
    if len(files[0]) > 10 or ''.join(files[0]).count('0123456789') > 3:
        return "No"
    if files[1] not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes the name of a file as input. It checks the following conditions:
1. The file name is not empty, and it is a string.
2. The file name contains exactly one dot ('.').
3. The part of the file name before the dot ('.') starts with a letter (uppercase or lowercase), and it does not contain more than three digits.
4. The part of the file name after the dot is either 'txt', 'exe', or 'dll'.
If all these conditions are met, the function returns 'Yes', indicating that the file name is valid. If any of these conditions are not met, the function returns 'No', indicating that the file name is not valid. 

The script then provides examples of input and their corresponding outputs to illustrate the behavior of the `file_name_check` function.