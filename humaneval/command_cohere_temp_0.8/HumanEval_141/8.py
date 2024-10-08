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

    latin_letter = False
    num_digits = 0
    dot_present = False
    file_extension = ""

    for char in file_name:
        if char.isdigit() and num_digits < 3:
            num_digits += 1
        elif char.isalpha():
            latin_letter = True
        elif char == ".":
            dot_present = True
        elif char == "txt" or char == "exe" or char == "dll":
            file_extension = char

    if not latin_letter:
        return "No"
    if dot_present == False or file_extension == "":
        return "No"

    return "Yes"
```

This Python script defines a function called `file_name_check` that checks if a given file name string conforms to a set of criteria specified by the docstring. The function analyzes the string and evaluates each criterion, returning "Yes" if all criteria are met and "No" if any of them are not met. It also provides informative messages for invalid file names.

This way, the code compactly encapsulates the entire problem in a single function, making it easy to use and integrate into larger projects.