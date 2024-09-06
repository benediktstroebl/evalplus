```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abcde')
    5
    >>> len('') == strlen('')
    True
    >>> ''.join().split('')
    [ '', ]
    >>> ['a', 'bb', 'ccc', 'dd', 'e'].count('c')
    2
    >>> 'a'.join('b')
    Traceback (None, ('AttributeError', None), None)
    """
    return len(string)
```