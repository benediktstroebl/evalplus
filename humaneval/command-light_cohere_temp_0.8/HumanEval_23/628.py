```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            TypeError: 'argument' 's' not iterable
        """
    if not iter(string):
        raise TypeError('argument must be iterable')
    length = 0
    for c in string:
        length += 1
    return length
```