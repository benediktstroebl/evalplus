```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') != 0
    False
    >>> 'hi' * 3 != strlen('hi')
    True
    >>> print('123')
    3
    """
    return len(string)
```