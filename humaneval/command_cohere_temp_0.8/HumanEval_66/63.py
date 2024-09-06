```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The `digitSum` function iterates through each character in the input string `s`. It filters out only the uppercase characters using the `isupper()` method and converts them to their corresponding ASCII integer codes using the `ord()` function. Afterwards, it sums up these ASCII codes to provide the final result.