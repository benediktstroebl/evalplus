```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a + a
    b = b + b
    return any(x in a for x in b.split())
```
The function leverages the repetition of the second word to check for substring occurrences. By concatenating the second word with itself and splitting it into individual characters, it can be rotated in all possible ways to check for substring occurrences in the first word. 

Would you like to test drive this script? Any additional problems we can help you solve?