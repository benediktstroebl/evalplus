```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abc__123')
        Error: invalid character ' '__' in the path of the string
        """
    return len(string)
```