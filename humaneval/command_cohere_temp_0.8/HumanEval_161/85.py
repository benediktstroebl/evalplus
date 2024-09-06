```python
def solve(s):
    new_str = []
    for c in s:
        if c.isalpha():
            new_str.append(c.swapcase())
        else:
            new_str.append(c)
    return ''.join(new_str)
```

This script defines a function `solve` that takes a string `s` as input and performs the tasks specified in the problem statement. It examines each character in the string using the `isalpha()` method. If it is an alphabetic character, it uses the `swapcase()` method to change its case, otherwise, it remains unchanged. A new string is constructed by appending the processed characters together, and finally, the function returns the resulting string.