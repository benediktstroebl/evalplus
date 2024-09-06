```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen(' ')
        2
        >>> strlen('\t')
        4
        >>> strlen('abc123')
        5
        """
    return len(string)
```