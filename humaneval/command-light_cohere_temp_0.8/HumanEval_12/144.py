Here's a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)
```
This function takes a list of strings as input and returns the longest string in the list, or None if the list is empty. It uses the Python's `max()` function with the `key=len` argument to return the string with the maximum length in the list.