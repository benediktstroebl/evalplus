```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns length of the string
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