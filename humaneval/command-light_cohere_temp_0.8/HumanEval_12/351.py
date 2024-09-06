```python
def longest(strings: List[str]) -> Optional[str]:
    """
    This function takes a list of strings and returns the longest string in the list.
    Parameters:
        strings: list of strings
    Returns:
        Optional[str] with the longest string or None if the list is empty or has no strings.
    """
    Test cases:
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest([])
    None
    >>> longest(['aa', 'aa'])
    'aa'
    """
    if not strings:
        return None
    return max(strings, key=len)
```