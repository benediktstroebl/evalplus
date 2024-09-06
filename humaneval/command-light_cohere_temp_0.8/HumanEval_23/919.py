```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abcabc')
    3
    >>> strlen('') + strlen('a')
    1
    >>> len('') < strlen('')
    True
    """
    return len(string)
```