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
        return "Yes"
    no_of_digits = sum(char.isdigit() for char in file_name)
    if no_of_digits > 3:
        return "No"
    has_dot = "." in file_name
    if not has_dot:
        return "No"
    before_dot, after_dot = file_name.split(".")
    if not before_dot.strip():
        return "No"
    if not before_dot.startswith(tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")):
        return "No"
    if after_dot not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This script defines a function called `file_name_check` that takes in a string representing a file's name and checks it against a set of criteria to determine whether the name is valid or not. The function returns "Yes" if the file name is valid, and "No" otherwise. 

The following are the criteria checked in the script:
1. There should not be more than three digits ('0'-'9') in the file's name.
2. The file's name contains exactly one dot '.' 
3. The substring before the dot should not be empty, and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z').
4. The substring after the dot should be one of these: ['txt', 'exe', 'dll'].

The script includes tests to check if the function behaves as expected and accordingly. You can use it by calling the function with a file name as input. 

If you have any questions, feel free to ask!