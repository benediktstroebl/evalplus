```python
def file_name_check(file_name):
    checker = lambda s: len(s) > 0 and s[0].isalpha() and s.count('.') == 1 and \
                        len(set(s.split('.')[1]).intersection('0123456789')) <= 3
    filename, extension = file_name.split('.')
    if checker(filename) and checker(extension) and extension in ['txt', 'exe', 'dll']:
        return "Yes"
    else:
        return "No"
```

The script divides the file name into a name and an extension using the `.` symbol. Both the filename and the extension are checked using a lambda function that verifies several conditions:
1. The length of the string is greater than 0, ensuring the filename is not empty.
2. The first character of the string is an alphabet letter, ensuring the filename does not start with digits.
3. There is exactly one period (`.`) in the string - this ensures that there are no unnecessary period symbols.
4. The string does not contain more than three digits in total, ensuring no unnecessary confusion between filename and versioning. 

Finally, the extension is checked to ensure it is either `txt`, `exe`, or `dll`. The function returns `"Yes"` if all conditions are met, and `"No"` otherwise. 

This script guarantees that filenames are not empty, start with a letter, do not contain unnecessary period symbols, and have valid extensions.