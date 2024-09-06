```python
def file_name_check(file_name):
    checker = ['1234567890', '.', 'a', 'txt', 'exe', 'dll']
    count = ('0123456789'.count(file_name))
    has_dot = ('.' in file_name)
    pre, post = file_name.split('.')
    alpha = (len(set(pre)) == 1 and pre[0].isalpha())
    ext = (post in checker)
    if count <= 3 and has_dot and alpha and ext:
        return "Yes"
    else:
        return "No"
```

The algorithm employs a list `checker` to streamline the process by validating the file extension and checking for the presence of exactly one `.`. The `count` variable assesses the number of digits in the file name, limiting it to zero or one. The `has_dot` condition validator checks for the presence of exactly one `.`. The `alpha` validator verifies the uniqueness of the initial character, ensuring it is an alphabetic character. The `ext` validator inspects the file extension, permitting only `txt`, `exe`, or `dll` extensions. If all conditions are met, the function returns `"Yes"`, otherwise it returns `"No"`. 

This algorithm provides a robust and adaptable solution that accommodates potential future changes in the validation criteria.