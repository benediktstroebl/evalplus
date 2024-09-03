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
    
    if not file_name.isalpha():
        return "FileName must start with a letter"
    
    dot_index = file_name.find(".")
    if dot_index < 0 or dot_index + 1 == len(file_name):
        return "File name should contain exactly one dot"
    
    prefix = file_name[:dot_index]
    
    if not prefix.isalpha():
        return "File name should start with a letter"
    
    if len(prefix) > 8 or len(prefix) == 0:
        return "The substring before the dot should have between (0-8) characters"
    
    if dot_index + 2 == len(file_name):
        return "The file's name should have at least two characters after the dot"
    
    suffix = file_name[dot_index + 1:]
    valid_suffix = ["txt", "exe", "dll"]
    if suffix not in valid_suffix:
        return "Valid file extensions are: txt, exe, dll"
    
    digits = sum(1 for c in file_name if c.isdigit())
    if digits > 3:
        return "File name should not contain more than three digits"
    
    return "Yes"
```

This code solves the problem statement by handling the various cases mentioned, such as checking for a single dot, alphabetic characters, and the number of digits. Finally, it returns "Yes" if the file name is valid and returns the reason if not. You can call this function with different file names to check for validity based on the given conditions.  This function can be added to a testing suite and verified with different test cases to ensure its correctness.  This approach assumes the file name is a string and that the file name conditions stated in the problem description apply.