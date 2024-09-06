```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen(' ')
        2
        >>> strlen('@')
        4
        >>> strlen(' Remaining text here')
        0
    """
    return len(string)
```