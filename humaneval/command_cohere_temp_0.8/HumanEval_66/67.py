```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```
This function uses the `ord()` function to get the ASCII value of each character in the string, and the `sum()` function to add them up. The `c.isupper()` condition is used to ensure that only the upper-case characters are considered for the digit sum.