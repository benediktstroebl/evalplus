```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            TypeError: 'callable' argument needed (got 'None')
    """
    if not string:
        raise TypeError('callable' argument needed)
    return len(string)
```