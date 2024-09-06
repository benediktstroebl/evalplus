```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') != 0
    False
    >>> len('') < strlen('')
    True
    """
    return len(string)
```