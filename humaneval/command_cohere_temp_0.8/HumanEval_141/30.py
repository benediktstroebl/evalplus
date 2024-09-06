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
        return "File name should be a string"

    if not file_name.startswith(tuple('aeiouAEIOU')):
        return "File name should start with a letter"

    latin_letter = file_name[0]
    ext = file_name.split(".")[1].lower() if "." in file_name else ""
    
    if len(set(file_name) & set("0123456789")) > 3:
        return "More than three digits in file name"

    if len(file_name.split(".")) != 2:
        return "Invalid file name. No dot '.'"

    if ext not in ['txt', 'exe', 'dll']:
        return "File extension should be either 'txt', 'exe' or 'dll'"

    return "Yes"
```

This code defines a function called `file_name_check` that takes a single argument, `file_name`, representing the name of a file. It checks the file name against a set of criteria to determine whether it is valid or not. The function returns a message saying "Yes" if the file name is valid, and a message explaining why it is not valid if it fails to meet the criteria. You can use this code to quickly check if a file name is valid or not by calling the function with the file name as argument.  The code is formatted with a docstring to describe the functionality and usage of the function, followed by the actual implementation.  It can be used to validate file names according to the specified rules.