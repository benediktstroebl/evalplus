```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    for i in range(1,len(b)+1):
        if b in a or b[i%len(b)] in a:
            return True
    return False
```