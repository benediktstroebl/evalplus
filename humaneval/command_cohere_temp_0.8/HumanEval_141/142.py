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

    # Define the maximum number of digits allowed in the file name (excluding extensions)
    max_digits = 3

    # Check for more than three digits in the file name (excluding extensions)
    if len(set(char for char in file_name if char.isdigit())) > max_digits:
        return "No"

    # Check for exactly one dot in the file name
    if ".." in file_name or "." not in file_name:
        return "No"

    # Split the file name into substring before and after the dot
    pre, ext = file_name.split(".")

    # Check that the substring before the dot starts with a letter
    if not pre or not pre[0].isalpha():
        return "No"

    # Check that the substring after the dot is in the list ['txt', 'exe', 'dll']
    if ext not in ["txt", "exe", "dll"]:
        return "No"

    return "Yes"
```

This Python script defines a function called `file_name_check` that takes the name of a file as input and returns either "Yes" or "No" depending on whether the file name meets a specific set of criteria. The function checks if the file name contains more than three digits, exactly one dot, and a valid prefix and extension. If all these conditions are met, it returns "Yes"; otherwise, it returns "No".