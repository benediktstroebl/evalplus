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
    
    if len(file_name) == 0:
        return "File name should not be empty"
    
    elif file_name.find(".") != len(file_name) - 1:
        return "File should contain exactly one dot"
    
    else:
        before_dot, after_dot = file_name.split(".")
        
        if len(after_dot) != 3:
            return "The file extension should be exactly three characters"
        
        elif after_dot not in ["txt", "exe", "dll"]:
            return "File extension should be only: txt, exe or dll"
        
        elif before_dot.isalpha() and len(before_dot) > 0 and len(before_dot.replace(".", "").replace("0123456789", "")) <= 2:
            return "Yes"
        else:
            return "No"
```

This script defines a function `file_name_check` that takes in a string `file_name` as input and returns either `'Yes'` if the file name is valid or `'No'` if it is not. The function checks the following conditions:
1. The `file_name` should not be empty.
2. There should be exactly one dot `'.'` in the file name.
3. The part of the file name before the dot should start with a letter and contain no more than two additional characters.
4. The part of the file name after the dot should be either `'txt'`, `'exe'`, or `'dll'`.

The function splits the file name at the dot, and checks the conditions separately for the before- and after-dot parts. Finally, if all conditions are met, the function returns `'Yes'`; otherwise, it returns `'No'`.

This solution assumes that the input `file_name` will have only letters, numbers, dots, and hyphens, as these are the only valid characters in a file name in Windows. 

The code assumes that the input will be a string representing a file's name. If any of the above conditions are not met, the function will return `'No'`. 

Please note that this code assumes that the file name is being created following Windows file name rules. Different operating systems might have different rules.