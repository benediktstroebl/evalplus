```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen(' ')
        2
        >>> strlen('abc123')
        5
        >>> strlen(' ') || 'cba')
        3
        >>> strlen(' 000000000')
        20
        """
    return len(string)
```