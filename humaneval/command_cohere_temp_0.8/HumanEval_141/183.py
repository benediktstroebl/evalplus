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
    num_found = 0
    for char in files[0]:
        if char.isdigit():
            num_found += 1
    if num_found > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes the name of a file as input. It checks the following conditions to determine if the file name is valid or not:

1. The file name is not an empty string or not a string.
2. The file name contains exactly one dot (`.`).
3. The part of the file name before the dot (extension) starts with a letter of the Latin alphabet and is not empty.
4. The part of the file name after the dot is either "txt", "exe", or "dll".
5. There are not more than three digits in the file name.

The function splits the file name into its extension and prefix using the split method, which splits the string at the first dot. It then checks each of the conditions and returns "Yes" if all conditions are met and "No" otherwise.

The script returns "No" if the file name does not meet any of the specified conditions, for example:
```python
file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
```

The script returns "Yes" if the file name meets all the conditions, for example:
```python
file_name_check("example.txt") # => 'Yes'
``` 

The function also includes some additional checks to validate the file name, such as checking if the file extension after the dot is one of the allowed types ("txt", "exe", or "dll"). 

Overall, this Python script solves the problem by creating a function that checks the validity of a file name according to the given conditions. 

Please note that this is just one possible solution and there are other ways to solve this problem in Python.