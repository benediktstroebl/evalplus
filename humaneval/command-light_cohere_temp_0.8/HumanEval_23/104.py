```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            ValueError: 'abc' not string'
        """
    if not str(string):
        raise ValueError('abc' not string')
    return len(string)
```