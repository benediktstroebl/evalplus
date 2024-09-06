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
    if len(files[0]) == 0 or not files[0][0].isalpha():
        return "No"
    if len(files[1]) != 4 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    if files[0].count("0123456789") > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which is a string representing the name of a file. This function returns a string that answers the question of whether the given file name is valid or not. 

The function checks the following conditions:
1. The file name is not empty and contains exactly one dot ('.').
2. The part of the file name before the dot contains letters and has a length of at least 1.
3. The part of the file name after the dot has a length of exactly 4 and is either "txt", "exe", or "dll".
4. There are not more than three digits in the file name.

The function splits the file name at the dot, and then checks each part of the file name for the necessary conditions. If all conditions are met, the function returns "Yes"; otherwise, it returns "No". 

This solution provides a clear and concise way of validating file names in accordance with the given problem statement.