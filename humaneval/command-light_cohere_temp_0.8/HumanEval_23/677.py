```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        4
        >>> strlen('')
        Error: empty string provided
        """
    if not string:
        raise Error("empty string provided")
    return len(string)
```