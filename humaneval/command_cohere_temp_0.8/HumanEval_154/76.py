```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    
    return second in first or any(x for x in first if x == second)
```
The function uses a list comprehension to check if any substring of the first word is equal to the second word. The case-insensitive comparison matches the words without considering character case. You can use this function to test against the provided examples. Let me know how you'd like to proceed!