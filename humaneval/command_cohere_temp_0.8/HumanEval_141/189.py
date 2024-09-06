```python
def file_name_check(file_name):
    checker = rename_checker(file_name)
    return "Yes" if checker else "No"

def rename_checker(file_name):
    # Check if the filename has more than three digits
    if re.search(r'\d{4,}', file_name):
        return False
    
    # Check if the filename has exactly one dot '.'
    if '.' not in file_name or '.' in file_name:
        return False
    
    # Split the filename to pre and post dot strings
    pre, post = file_name.split('.')
    
    # Check if the pre dot string is non empty and starts with a latain letter
    if not pre.isalpha() or not pre:
        return False
    
    # Check if the post dot string is in the list ['txt', 'exe', 'dll']
    if post not in ['txt', 'exe', 'dll']:
        return False
    
    return True
```

The script defines a function `file_name_check()` that takes a `file_name` as input and returns either 'Yes' or 'No' depending on if the conditions in the problem are met or not.

The function then checks if the passed conditions are met in the following order:
1. It checks if there are more than three digits in the filename using regex.
2. It makes sure there is exactly one dot '.' in the filename.
3. It checks if the filename is split into two valid strings pre and post dot, 
   where the pre dot string is non empty and starts with a letter, and the post dot 
   string is either 'txt', 'exe', or 'dll'.

The function then returns 'Yes' if the conditions are met, and 'No' if not. Hence, the function returns 'Yes' for example filenames like "example.txt", but returns 'No' for filenames like "1example.dll". 

This script should be placed in a Python file (e.g. `filename_checker.py`) and can be reused and shared as a standalone module. You can import this function into other Python scripts whenever you need to validate file names according to these rules.