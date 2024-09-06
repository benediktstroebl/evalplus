```python
def file_name_check(file_name):
    lambda_string = lambda s: len(s) <= 3 and s.isalpha() and s[:1].isalpha() and s[-1] == '.'
    lambda_func = lambda s, l: s == '.' or (l == 'txt' or l == 'exe' or l == 'dll')
    if lambda_string(file_name) and lambda_func(file_name[1:], file_name[3:]):
        return "Yes"
    else:
        return "No"
```

This Python script defines a lambda function for each condition mentioned in the problem statement. These lambda functions are used to validate various conditions independently. Finally, the script checks if all conditions are satisfied by using these lambda functions. The return statement returns "Yes" if the file name is valid, and "No" otherwise. 

Note that the code assumes that the file name provided as input is already sanitized and does not contain any special characters other than the specified ones. If the file name contains any special characters, they should be removed or handled appropriately before passing them to this function.