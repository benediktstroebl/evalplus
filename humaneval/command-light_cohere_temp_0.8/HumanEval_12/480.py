Here is a self-contained Python function that returns the longest string in a list of strings:
```python
def longest(strings: List[str]) -> str:
    if not strings:
        return None
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string using the `max()` function with the `len` function as the key argument. It also handles the important test case of an empty input list, returning `None`.