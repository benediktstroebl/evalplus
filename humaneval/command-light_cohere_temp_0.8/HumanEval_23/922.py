```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        4
        >>> strlen('abc123')
        5
        >>> strlen('') == 0
        True
        """
    if not string:
        return 0
    return len(string)
```