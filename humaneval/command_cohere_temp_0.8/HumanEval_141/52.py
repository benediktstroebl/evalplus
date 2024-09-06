```python
def file_name_check(file_name):
    checks = []
    
    # Check if there's more than three digits in the filename
    digits = '[0-9]{4,}'
    if re.search(digits, file_name):
        return 'No'
    
    # Check for exactly one dot in the filename
    if '.' not in file_name or '.' in file_name twice:
        return 'No'
    
    # Check if the substring before the dot starts with a letter
    pre_dot = file_name[:file_name.index('.')]
    if not pre_dot.isalpha():
        return 'No'
    
    # Check if the substring after the dot is amongst the specified values
    post_dot = file_name[file_name.index('.')+1:]
    if post_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    checks += [bool(re.search(digits, file_name)) == False, 
              '.' in file_name exactly once, 
              pre_dot.isalpha() and post_dot in ['txt', 'exe', 'dll']]
    
    return 'Yes' if all(checks) else 'No'
```

The Python script defines a function `file_name_check` that takes a `file_name` as input, which is a string representing a file's name. This function returns 'Yes' if the file's name is valid, and 'No' otherwise.

The function examines the file's name based on several conditions outlined in the problem statement:
1. It should not contain more than three digits.
2. It should contain exactly one dot '.'.
3. The substring before the dot should start with a letter (lower or uppercase) from the Latin alphabet.
4. The substring after the dot should be either 'txt', 'exe', or 'dll'.

The script employs regular expression (`re.search`) and string methods (`isalpha`, `index`, `slice`) to check the file name against these conditions and gathers the results in a list `checks`. It then uses the `all` function to evaluate whether all checks passed, which determines whether the file name is valid or not. 

The script is self-contained and can be directly copied and run, as it does not depend on any external modules or libraries other than what's available by default in Python. 

You can test this function by calling it with different file names to see the validation behavior for different cases. You can also edit the function to include or remove conditions to tighten or relax the validation rules accordingly.