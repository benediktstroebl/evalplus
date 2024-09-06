```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' ')
    2
    >>> strlen('   ')
    0
    >>> strlen('  23')
    10
    >>> strlen('abcabc')
    4
    """
    return len(string)
```