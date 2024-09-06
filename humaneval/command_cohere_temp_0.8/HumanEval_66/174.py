```python
def digitSum(string):
    return sum(ord(c) for c in string if c.isupper())
```
This function uses the `ord()` function to get the ASCII value of each character in the string, and the `sum()` function to add them up. The `c.isupper()` condition ensures that only the upper-case characters are considered for the digit sum.