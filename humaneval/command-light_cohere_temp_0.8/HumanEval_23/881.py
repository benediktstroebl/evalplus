```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            TypeError: 'argument' 'squeeze' expected string or buffer
        """
    return len(string)
```