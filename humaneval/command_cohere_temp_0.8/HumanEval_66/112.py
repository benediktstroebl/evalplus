```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The `digitSum` function iterates through each character in the string `s`. It ignores non-alphabetical characters and calculates the sum of the ASCII values for uppercase letters. The resulting output is the sum of the ASCII values of the digits present in the string.