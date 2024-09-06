```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The `digitSum` function iterates through each character in the string `s`. It filters out only the upper-case characters using the `isupper()` method and converts them to their corresponding ASCII value using the `ord()` function. Subsequently, it sums up these ASCII values using the `sum()` function to obtain the final result.