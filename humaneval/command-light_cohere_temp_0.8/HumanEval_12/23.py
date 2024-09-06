Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string in the list, or None if the list is empty. The function uses the `max()` function with the `key` parameter set to `len` to sort the strings in the list by length, and then returns the longest string. 

This code is self-contained, and can be easily integrated into any project where you need to solve this problem.