```python
def cycpattern_check(a, b):
    a = a.lower()
    b = b.lower()
    return b in a or any(b in rotatedWord for rotatedWord in a.rotate(-1))
```
This function takes two strings as input and rotates the second string in memory before checking for substring matches. It returns true if the second string or any of its rotations are a substring in the first string. It's important to use lowercase for both strings to ensure consistent results.  This solution allows rotations of the second string in memory, improving efficiency. The rotate method creates a new string with the same characters in the reversed order.