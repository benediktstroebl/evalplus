Here's a self-contained Python function that solves the problem:
```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Find the longest string from a list of strings.
    Args:
        strings (list of strings): List of strings.
    Returns: The longest string in the list.
    Returns: None if the list is empty.
    """
    List of strings is possibly allowed to contain duplicate characters.
    """
    using the longest(strings)
    """
    if not strings:
        return None
    return max(strings, key=len)
```
This function takes a list of strings as input and returns the longest string in the list, or None if the list is empty.