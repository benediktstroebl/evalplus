Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Find the longest string in the list.
    Parameters:
        strings: list of strings
    Returns:
        The longest string, or None if empty list
    """
    if not strings:
        return None
    return max(strings, key=len)
```

This code defines a function `longest` that takes a list of strings as an argument and returns the longest string in the list, or `None` if the list is empty. It uses the tested with the key=len function to find the largest string in the list, which is of course the longest.