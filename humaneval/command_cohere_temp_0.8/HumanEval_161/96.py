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

The function `solve` takes a string as its argument and iterates through it. In each iteration, we check if the current character is alphanumeric using the `isalpha()` function. If true, we use the `swapcase()` method to change the case of the character. Otherwise, we add it to the new string as it is. Finally, we return the resulting string.