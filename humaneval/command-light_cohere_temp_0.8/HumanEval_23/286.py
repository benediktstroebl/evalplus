```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('0000')
        20
        >>> strlen(' ')
        1
        >>> strlen('   ')
        2
        """
    return len(string)
```