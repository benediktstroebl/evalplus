```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The function `digitSum` works by using a generator expression, created by using the `ord()` function on each character in the string `s` if the character is upper case. These codes are then summed using the `sum()` function. The generator expression and the sum function handle the strings of different lengths and characters correctly, resulting in a numeric value representing the sum of the upper case characters' ASCII codes in the string.