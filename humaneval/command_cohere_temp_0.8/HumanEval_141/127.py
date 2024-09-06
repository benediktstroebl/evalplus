```python
def file_name_check(file_name):
    dig_count = file_name.count('0123456789')
    dot_count = file_name.count('.')
    
    if dot_count == 1 and dig_count <= 3 and len(file_name) > 1:
        pre, ext = file_name.split('.')
        if len(pre) > 0 and pre[0].isalpha() and ext in ['txt', 'exe', 'dll']:
            return 'Yes'
    return 'No'
```

This Python script defines a function called `file_name_check` that takes a string representing a file name as input. It checks the file name against a set of criteria to determine whether it is valid or not, and returns 'Yes' or 'No' accordingly.

The criteria are that there should be no more than three digits (0-9) in the file name, there should be exactly one dot ('.'), the substring before the dot (pre) should not be empty and it should start with a letter (lower or uppercase A-Z), and the substring after the dot should be one of ['txt', 'exe', 'dll']. 

The function splits the file name at the dot into pre and ext using the split() method, and then checks for the validity criteria. 

It returns 'Yes' if all criteria are met, and 'No' otherwise. 

This solution provides a clear and concise way to check file name validity based on the given specifications. 

You can use this function in other parts of your code by calling it and passing the file name you want to check.  It can also be easily adapted to accommodate additional checks or exceptions as needed.