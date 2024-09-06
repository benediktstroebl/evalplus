```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    return second in set([x for x in first.split(' ') if x]) or any(second == x for x in first.split(' ') if x)
```