```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The function `digitSum` leverages Python's built-in function `sum` along with a list comprehension that traverses each character in the string `s`. The comprehension filters out only the uppercase letters, which are then passed through the `ord` function to retrieve their corresponding ASCII code values. These codes are added together using the `sum` function, resulting in the required sum of the upper characters' ASCII codes.

This approach effectively solves the problem while maintaining a concise and efficient solution. Let me know if you'd like to further discuss any part of the code!