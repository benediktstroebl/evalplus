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

This Python script defines a function called `file_name_check` that takes the name of a file as input. It checks the validity of the file name based on several conditions:

1. The input should be a non-empty string.
2. It should contain exactly one dot (`.`).
3. The substring before the dot should start with a letter (upper or lower case) and cannot be empty.
4. The substring after the dot should be one of the following: "txt", "exe", or "dll".
5. There should not be more than three digits (0-9) in the file name.

If any of these conditions are not met, the function returns "No", indicating that the file name is not valid. Otherwise, it returns "Yes" to indicate that the file name is valid.

The function then uses regular expressions to check for the presence of a single dot and validates the character after the dot and the number of digits. Finally, it returns a 'Yes' if the name satisfies all these conditions, and 'No' otherwise.