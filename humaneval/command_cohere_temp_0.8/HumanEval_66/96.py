```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The `digitSum` function iterates through each character in the input string `s`. It filters out only the upper-case characters using the `isupper()` method and converts them to their corresponding ASCII integer codes using the `ord()` function. Subsequently, it sums up these integer values, providing the total of the upper-case characters' ASCII codes as the function's output.