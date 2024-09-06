```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The function `digitSum` sums the ASCII values of all uppercase characters in the input string `s`. To avoid converting the entire string to uppercase, which could be slow for long strings, the function uses a generator expression alongside the `isupper()` string method to only extract the uppercase characters, which greatly improves efficiency. 

To get the ASCII value for each character, the `ord()` function is used which returns the corresponding ASCII code for the character. These sums are then aggregated using the `sum()` function. 

This solution is concise and efficient, making use of Python's intrinsic string methods and idiomatic syntax to accomplish the task.