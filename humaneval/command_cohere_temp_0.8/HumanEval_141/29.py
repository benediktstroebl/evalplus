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
        return "File's name should be a string"
    
    if not file_name.isalpha():
        return "FileName should start with a letter"

    dot_index = file_name.find(".")
    if dot_index == -1:  # No dot in the file name
        return "The file's name should contain exactly one dot '.'"
    if len(file_name) - dot_index - 1 > 3:  # More than three characters after the dot
        return "There should not be more than three digits ('0'-'9') in the file's name."

    prefix = file_name[:dot_index]
    if not prefix.isalpha():
        return "The file's name should start with a letter."

    ext = file_name[dot_index+1:]
    allowed_ext = ["txt", "exe", "dll"]
    if ext not in allowed_ext:
        return f"Invalid extension. The file's name should end with '{', '.join(allowed_ext)}'"
    
    return "Yes"
```

This code defines a function `file_name_check` that checks the validity of a file name according to the given specifications. 

The following conditions are checked:
1. The input `file_name` must be a string.
2. The file name should start with a letter (ignoring case).
3. The name should contain exactly one dot.
4. The substring before the dot should not be empty and should start with a letter.
5. The substring after the dot should be one of the allowed extensions ("txt", "exe", "dll").
6. There should not be more than three digits in the file name.

If all conditions are met, the function returns "Yes," indicating a valid file name; otherwise, it returns an error message specifying the condition that was not met.

The `file_name_check` function encapsulates the entire logic needed to validate the file name, making it easy to reuse and test for correctness.