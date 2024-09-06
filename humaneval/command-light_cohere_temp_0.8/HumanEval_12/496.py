Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> str:
    if not strings:
        return None
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string in that list. The function returns `None` if the input list is empty.

The `max` function along with the `key=len` argument is used to identify the longest string in the list. This ensures that the longest string among a list of strings of the same length will be chosen.