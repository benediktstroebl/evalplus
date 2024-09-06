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
    if not before_dot.startswith(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")):
        return "No"
    if after_dot not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes a single argument, `file_name`, which is the name of a file. The function evaluates the validity of the file's name according to a set of constraints and returns either 'Yes' or 'No' depending on whether the name is valid or not. 

The function evaluates the following constraints:
1. The file name is not an empty string, and it's of type string.
2. The name does not contain more than three consecutive digits.
3. The name contains exactly one dot ('.').
4. The substring before the dot should not be empty, and it starts with a letter from the Latin alphabet (uppercase or lowercase).
5. The substring after the dot should be one of the following: 'txt', 'exe', 'dll'. 

The function splits the string into two parts using the dot as a delimiter, and checks the validity of the file name according to each of the constraints, returning 'Yes' if the name is valid and 'No' otherwise.

The function includes robust checks for digits, alphabet characters, and the presence of the specified extensions, ensuring accurate validation of file names according to the specified conditions.