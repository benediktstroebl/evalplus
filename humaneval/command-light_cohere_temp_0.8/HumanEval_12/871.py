```python
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.

    Returns the string if list is empty, or the list contains strings of different lengths.

    Otherwise, return None.

    >>> longest([])

    # Empty list
    >>> longest([]) is None
    >>> longest(["a", "bb", "ccc"])
    'ccc'
    >>> longest(["a", "bc", "abc"])
    'abc'
    """
    if not strings:
        return None
    max_length = max(len(x) for x in strings)
    return strings[0].rstrip('[]')[:max_length]
```