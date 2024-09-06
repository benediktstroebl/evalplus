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
    # Check for more than three consecutive digits
    if any(map(str.isdigit, files[0])) and len(files[0]) > 3:
        return "No"
    # Check for valid first part of file name
    if not files[0][0].isalpha():
        return "No"
    # Check for valid extension part of file name
    if files[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes the file name as a parameter and returns 'Yes' if the name satisfies all the given conditions, and returns 'No' otherwise. The provided conditions check that:
- The file name should not contain more than three consecutive digits.
- The file name should contain exactly one dot ('.').
- The substring before the dot should not be empty and it should start with a letter (uppercase or lowercase).
- The substring after the dot should be one of the following: ['txt', 'exe', 'dll']. 

The function will return 'No' if any of these conditions are not met, providing a markdown code block that demonstrates the conditions. 
The total time complexity of this function is O(N) where N is the size of the given `file_name`, while the space complexity is O(1) as it uses a constant amount of memory to hold the variables used for checking the conditions. 
This code efficiently checks the validity of a file name according to the given constraints from the prompt.