```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```
This function uses the `sum()` function in Python to add up the upper characters only, using the `ord()` function to get the ASCII value of each character in the string, and filters out non-uppercase characters using the `isupper()` string method. This results in the total value of the uppercase letters' ASCII values.