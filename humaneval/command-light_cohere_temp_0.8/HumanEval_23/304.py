```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('spaces')
    4
    >>> strlen('uttering text')
    11
    >>> strlen('abc123')
    12
    >>> len('abc')
    3
    >>> len('') == 0
    True
    """
    return len(string)
```