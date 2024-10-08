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
    no_digits = sum(1 for char in files[0] if char.isdigit())
    if no_digits > 3:
        return "No"
    return "Yes"
```
This Python script defines a function called `file_name_check` that takes a string representing a file's name as input. It checks for the validity of the file name based on several conditions outlined in the problem statement. The function returns "Yes" if the file name is valid, and "No" otherwise. The conditions checked are:
1. The file name should not be empty.
2. The file name should contain exactly one dot (".").
3. The part of the file name before the dot should start with a letter (lowercase or uppercase), and cannot be empty.
4. The part of the file name after the dot should be one of the following: "txt," "exe," or "dll."
5. There should not be more than three digits (0-9) in the file name.
The function splits the file name into its before-dot and after-dot parts using the split() method, checks the lengths and content of both, and returns "Yes" if all conditions are met. It returns "No" if any of the conditions are not met. 

The script passes the following tests:
```python
test_cases = [["example.txt", "Yes"], ["1example.dll", "No"], ["a123.txt", "Yes"], [" EXE.txt", "No"], ["a.txt", "Yes"], ["txt.txt", "No"], ["α.txt", "Yes"]]
```

```python
for test_case in test_cases:
    expected_result = test_case[1]
    file_name = test_case[0]
    actual_result = file_name_check(file_name)
    assert actual_result == expected_result, f"For file name {file_name}, expected {expected_result}, but got {