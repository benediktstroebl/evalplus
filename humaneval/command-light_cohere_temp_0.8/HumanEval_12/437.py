Here's a self-contained Python function that returns the longest string from a list of strings:
```python
def longest(strings: List[str]) -> str:
    if not strings:
        return None
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string using the `max` function with the `key=len` argument, which compares the length of each string to be the longest. It also handles the
 empty input list, returning `None`.