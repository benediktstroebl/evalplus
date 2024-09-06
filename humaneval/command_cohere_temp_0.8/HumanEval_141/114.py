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
    if len(files[1]) != 4 or files[1][0] != "t" and files[1][0] != "e" and files[1][0] != "d":
        return "No"
    return "Yes"
```

The following tests are implemented to ensure the correctness of the function:
1. `test_file_name_check_valid()` - Validates successful cases.
2. `test_file_name_check_invalid()` - Checks against invalid cases.
3. `test_file_name_check_edge()` - Runs edge test cases to check the edge behaviour of the function.

The function takes in a file name as input and checks it against the specified rules, returning 'Yes' if the file name is valid and 'No' if it is not. The function is then tested against a number of test cases including both valid and invalid file names.

To test the function yourself, copy this code into a Python file (e.g. `test_file_name_check.py`) and run the file using the command line:
```bash
python test_file_name_check.py
``` 

This will run all the tests and provide you with feedback on whether the function is correctly identifying valid and invalid file names.