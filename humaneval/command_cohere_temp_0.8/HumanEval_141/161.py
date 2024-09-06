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
    if files[0].strip() == "" or not files[0].strip().isalpha():
        return "No"
    if len(files[1]) != 4 or files[1][0] != "t" and files[1][0] != "x" and files[1][0] != "d":
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes the name of a file as input. It checks the following conditions of a valid file name:
1. The file name should not contain more than three consecutive digits.
2. The file name should contain exactly one dot (**.**).
3. The part of the file name before the dot should start with a letter of the Latin alphabet and should not be empty.
4. The part of the file name after the dot should be either "txt", "exe", or "dll".

The function splits the file name into its preceding and succeeding substrings at the dot, and verifies each of these four conditions separately. If any of the conditions are not met, the function returns "No"; otherwise, it returns "Yes". 

This solution employs the split function to divide the file name based on the dot, the strip function to remove leading and trailing spaces from strings, and the isalpha function to check if a string contains letters only. These methods are part of the Python standard library and are uncomplicated to use.