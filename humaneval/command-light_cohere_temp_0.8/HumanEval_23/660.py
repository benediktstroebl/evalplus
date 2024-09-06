```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') == 0
    True
    >>> len('') < strlen('')
    True
    >>> "asdfadsf" == "abcdef"
    False
    """
    return len(string)
```