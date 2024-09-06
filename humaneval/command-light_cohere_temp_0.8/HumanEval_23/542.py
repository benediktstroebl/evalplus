```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') + strlen('abc')
    3
    >>> str.join('') == strlen('')
    True
    >>> 997 == strlen('abc')
    False
    """
    return len(string)
```