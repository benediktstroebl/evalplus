```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: Length of the given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc123')
    5
    >>> strlen('') == 0
    True
    >>> len('') > strlen('')
    True
    """
    return len(string)
```