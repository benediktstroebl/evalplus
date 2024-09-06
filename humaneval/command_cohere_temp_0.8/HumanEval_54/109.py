Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / max(len(s0), len(s1)) > 0.5
```
The function `same_chars()` takes two strings as input and returns a boolean indicating whether the two strings have the same characters. The function uses the `set` method to remove duplicate characters from both strings and then calculates the ratio of matching characters to the maximum length of the two strings. If this ratio exceeds 0.5, it returns `True`, indicating that the strings have substantially the same characters, whereas if it is less than 0.5, it returns `False`, indicating that they do not.  This approach allows the function to handle various cases of capital and lower case letters, as well as multiple versions of strings where the order of characters is scrambled.