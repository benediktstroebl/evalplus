```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abcde')
    5
    >>> strlen(' ')
    1
    >>> strlen('  )')
    ZeroDivisionError: 'str.__len__()' overflow: long integer value '?'
        Traceback (most recent call last):
            ...
    """  
    return len(string)
```