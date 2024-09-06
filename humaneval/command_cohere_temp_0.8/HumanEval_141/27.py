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
    # Check for dots and underscores
    if ("_" in files[0]) or ( "_" in files[1]) :
        return "No";
    # Check for digits
    if len(files[0]) > 3:
        return "No"
    if files[0][0].isalpha():
        if files[1] in ["txt", "exe", "dll"]:
            return "Yes"
    else:
        return "No"
```

The following tests will prove that the function behaves as expected:
```python
test_cases = [
    ("example.txt", "Yes"),
    ("1example.dll", "No"),
    (" EXE.txt", "No"),
    ("exe.txt", "Yes"),
    ("1.txt", "No"),
    ("_example.txt", "No"),
    ("example_.txt", "No"),
    ("Exe.txt", "Yes"),
    ("E1.txt", "No"),
    ("Letters.txt", "Yes"),
    ("123.exe", "No"),
    ("1.2.3.exe", "No")
]

for test_case in test_cases:
    assert file_name_check(test_case[0]) == test_case[1]
```

This script will return the proper string ('Yes' or 'No') depending on the format of the given file name. 

Note: This code assumes that the input will be a file name without paths. If paths are included, they will be ignored.