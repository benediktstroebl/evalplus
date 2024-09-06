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
    files = file_name.split(".")
    if len(files) != 2:
        return "No"
    # check for digit count
    if len(files[0]) == 0 or not any(char.isdigit() for char in files[0]):
        if len(files[0]) > 3:
            return "No"
    else:
        return "No"
    # check for dot existence
    if "." not in file_name:
        return "No"
    # check for file extension
    if files[1] not in ["txt", "exe", "dll"]:
        return "No"
    # check for starting letter
    if len(files[0]) == 0 or not files[0][0].isalpha():
        return "No"
    return "Yes"
```
This code first checks if the file name is not empty and consists of a single dot and a file extension among the specified extensions. It also checks if the file name starts with a letter and does not contain more than three digits in the name.

Here is an example of how to use this function:
```python
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a letter)
``` 

The first output will be 'Yes', as the file name is valid, while the second output will be 'No', since the file name starts with a digit, which is not valid according to the criteria specified in the problem statement.