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
    if len(files[1]) != 4 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    no_of_digits = 0
    for char in files[0]:
        if char.isdigit():
            no_of_digits += 1
    if no_of_digits > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which is the name of a file. This function returns the string "Yes" if the specified file name meets a set of criteria, and the string "No" otherwise. The criteria are:
1. The file name is not empty, and it is a string.
2. The file name contains exactly one dot (`.`).
3. The part of the file name before the dot (`.`) starts with a letter of the Latin alphabet and is not empty.
4. The part of the file name after the dot (`[]) is one of the three specified strings: `txt`, `exe`, or `dll`.
5. There are not more than three digits (0 to 9) in the file name.

The function checks each of these criteria and returns the appropriate response ("Yes" or "No") based on the results.

This solution is concise, and uses native Python functionalities like `isalpha()`, `isdigit()`, `split()` and string properties for efficient filtering and logic, which makes it execute efficiently without any external dependencies.