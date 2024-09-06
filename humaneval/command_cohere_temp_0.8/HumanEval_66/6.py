```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The `digitSum` function iterates through each character in the string `s`. It ignores non-alphabetical characters and only takes uppercase letters, converting each one to its numerical ASCII code using the `ord()` function. Afterward, it sums all these numerical values and returns the result.