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
    if not isinstance(file_name, str):
        return "File name should be a string!"

    latin_char_count = 0
    digit_count = 0
    dot_count = 0
    valid_extension = False

    for char in file_name:
        if char.isalpha():
            latin_char_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char == ".":
            dot_count += 1
        elif char == "txt" or char == "exe" or char == "dll":
            valid_extension = True

    if latin_char_count == 0:
        return "No"
    if dot_count != 1 or latin_char_count == 1:
        return "No"
    if digit_count > 3:
        return "No"
    if not valid_extension:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes a `file_name` as input and returns 'Yes' if the file name is valid, and 'No' otherwise, based on certain conditions such as the number of digits, the presence of exactly one dot, valid start letters, and specified extensions. The conditions are checked using loops and if statements, and the function returns the appropriate response based on the evaluated conditions.