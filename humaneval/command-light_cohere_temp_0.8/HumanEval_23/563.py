```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            TypeError: 'str' object does not support item assignment
        """
    if not string:
        return 0
    return len(string)
```