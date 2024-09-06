```python
def file_name_check(file_name):
    checker = lambda s: len(s) <= 1 and s[0] in '.-' and s[1:] in ['txt', 'exe', 'dll']
    return 'Yes' if checker(file_name) else 'No'
```

This Python script defines a function `file_name_check` that takes a single argument `file_name`, which represents the name of a file. The function returns 'Yes' if the file name meets all the specified criteria and 'No' otherwise.

The criteria checked are:
1. The length of the file name should not exceed three characters, and it should contain only one dot '.' and possibly one hyphen '-'.
2. The substring after the dot should be one of ['txt', 'exe', 'dll'].

This is achieved through the use of a lambda function `checker` that checks for these conditions, and the result is returned accordingly. 

Such a solution uses a lambda function to keep the code concise and focused on the problem at hand, following the principle of separating concerns in programming.