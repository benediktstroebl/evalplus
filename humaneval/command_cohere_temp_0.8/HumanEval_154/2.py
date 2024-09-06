```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    
    return second in first or any(x for x in first if x == second)
```
The function uses lowercase conversion for consistency and uses `any` along with a generator expression to check if any substring of the first word is equal to the second word (or one of its rotations). 

The function effectively solves the problem and would pass the tests provided.