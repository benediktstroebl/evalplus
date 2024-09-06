```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abcabc')
    6
    >>> strlen('') == 0
    True
    >>> strlen('x' + 'y')
    Trace Interview Error
    'x' + 'y' not in string
    """
    return len(string)
```