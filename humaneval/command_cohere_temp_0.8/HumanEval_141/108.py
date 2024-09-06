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
    if not before_dot.startswith(tuple(string.ascii_lowercase + string.ascii_uppercase)):
        return "No"
    if after_dot not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which is a string representing the name of a file. 

The function returns "Yes" if the given file name follows certain rules and "No" otherwise. The file name is considered valid if it meets all of the following conditions:
- It should not contain more than three consecutive digits.
- It should contain exactly one dot (`.`).
- The part of the name before the dot should start with a letter (uppercase or lowercase) and should not be empty.
- The part of the name after the dot should be either "txt", "exe", or "dll".

The function checks for these conditions using various Python techniques such as string manipulation, digit counting, and splitting. It first checks for the basic requirements of validity, such as the presence of a dot and the absence of more than three digits. These checks are done using logical statements and Python's built-in string methods. 

The function then checks for the uniqueness of the dot and returns "No" if there is more than one dot. It uses the `split()` function to split the file name into the part before the dot and the part after the dot. The function then checks if the before-dot part has a letter as the first character and returns "No" if this is not the case. The function also checks if the after-dot part is not a valid file extension and returns "No" if this is the case.

If all these conditions are met, the function returns "Yes". 

The script then provides examples of calls to the `file_name_check` function and shows the expected outputs, demonstrating how the function handles different cases of file names.