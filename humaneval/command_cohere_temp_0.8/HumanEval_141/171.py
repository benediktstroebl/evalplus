```python
def file_name_check(file_name):
    checker = lambda s: len(s) > 0 and s[0].isalpha() and s.count('.') == 1 and \
                       sum(c.isdigit() for c in s) <= 3 and \
                       (s.split('.')[-1] in ['txt', 'exe', 'dll'] or s.split('.')[-2] in ['txt', 'exe', 'dll'])
    return 'Yes' if checker(file_name) else 'No'
```

This Python script defines a function called `file_name_check` that takes in a string representing a file name as input. It checks for five criteria to determine the validity of the file name:
1. The length of the string should be greater than 0 (ensuring it's not an empty string).
2. The first character of the string should be a letter (uppercase or lowercase) to simulate the requirement of a valid file name starting with a letter.
3. The string should have exactly one occurrence of the dot character (`.`) to ensure it follows the typical file extension format.
4. The string should not have more than three digits in total (to ensure no more than three digits in the file name or extension).
5. The file extension (the part after the dot) should be either `txt`, `exe`, or `dll` if it is the last segment after splitting by dot, or it can be any of these three options if considered the second last segment after splitting by dot.

The function uses a lambda function (`checker`) as a filter to check each condition. If all conditions are met, the function returns 'Yes', indicating a valid file name; otherwise, it returns 'No'.

This solution provides a clear and concise approach to validating file names using Python.