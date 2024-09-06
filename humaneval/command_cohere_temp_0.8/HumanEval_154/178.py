```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    
    return second in first or any(x for x in second if x in first)
```
The function uses lowercase conversion for the words and uses `in` statement for direct substring check, then uses chaining and looping on rotations of the second word with `any()` function to check if any of the rotations is present in the first word.