```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```
This function uses the `sum()` function in Python to add up the upper characters only, using the `ord()` function to get the ASCII value of each character and filtering out non-uppercase characters using the `isupper()` method. These methods allow the function to correctly calculate the sum of the upper characters' ASCII codes in the provided strings.