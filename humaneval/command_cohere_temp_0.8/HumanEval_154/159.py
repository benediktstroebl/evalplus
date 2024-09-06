```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    for i in range(0, len(b)):
        if a.find(b[i:]) != -1 or a.find(b[i:] + b[:i]) != -1:
            return True
    return False
```