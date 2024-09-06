```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abc123')
        5
        >>> strlen(' ')
        0
        >>> strlen('')
        <ValueError: str.len() expected argument str, not str in (string, bytearray, bytes)
        """
    return len(string)
```