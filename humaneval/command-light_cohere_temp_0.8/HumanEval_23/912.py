```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen(' ''')
        0
        >>> strlen('  myst')
        4
        """
    return len(string)
```