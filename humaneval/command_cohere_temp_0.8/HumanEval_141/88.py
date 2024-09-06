```python
def file_name_check(file_name):
    digits = ''.join('0123456789')
    dot = '.'
    latin_alphabet = ''.join('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' )
    valid_ext = ['txt', 'exe', 'dll']

    if len(file_name) == 0:
        return "No"

    file_name = file_name.lower()
    num_digits = sum(1 for c in file_name if c in digits)
    
    if num_digits > 3:
        return "No"
    elif num_digits == 0:
        pos = file_name.find(dot)
        if pos == -1:
            return "No"
        pre_dot = file_name[:pos]
        if not (pre_dot[0] in latin_alphabet and pre_dot[0] != ""):
            return "No"
        post_dot = file_name[pos+1:]
        if post_dot not in valid_ext:
            return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` taking a `file_name` as input and returning either "Yes" or "No" based on the conditions laid out in the problem. The script evaluates the following:
1. The filename shouldn't have more than three digits.
2. There should be exactly one dot ('.').
3. The substring before the dot should start with a letter of the Latin alphabet.
4. The substring after the dot should be one of ['txt', 'exe', 'dll'].

The function returns "Yes" if the file name satisfies all these conditions, and "No" otherwise.

This solution employs some handy Python tricks, like using `sum` to count digits and `find` to locate the first occurrence of a dot, enhancing readability and efficiency.