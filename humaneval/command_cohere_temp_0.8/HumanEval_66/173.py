```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```
This function uses the `sum()` function in Python to add up the upper characters ASCII codes only if the character is upper case. This is done using a generator expression alongside the `ord()` function which returns the ASCII code of a character, and the `isupper()` string function to check if the character is upper case.