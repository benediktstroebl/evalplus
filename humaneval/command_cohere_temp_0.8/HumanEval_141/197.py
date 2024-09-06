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
    if len(files) != 2 or not files[0]:
        return "No"
    if len(files[0]) == 0 or not (files[0][0].isalpha() or files[0][0].isupper()):
        return "No"
    if len(files[1]) != 3 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    no_of_digits = 0
    for char in files[0]:
        if char.isdigit():
            no_of_digits += 1
    if no_of_digits > 3:
        return "No"
    return "Yes"
```

This script defines a function `file_name_check` that takes in a string representation of a file name as an input. It checks for five criteria to determine the validity of the file name:
1. The input string should not be empty or not equal to the file name.
2. The file name should contain exactly one dot (.).
3. The substring before the dot should not be empty and should start with a letter (lowercase or uppercase).
4. The substring after the dot should be one of the following: "txt", "exe", or "dll".
5. There should not be more than three digits (0-9) in the file name.

The function splits the file name into its before and after-dot substrings and checks the above conditions. If all conditions are satisfied, the function returns "Yes"; otherwise, it returns "No".

This solution aims to provide a clear and concise way to validate file names based on the specified conditions, ensuring both accuracy and readability. 
```