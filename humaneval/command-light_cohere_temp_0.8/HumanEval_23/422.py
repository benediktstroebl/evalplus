```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abc') != 3  # should return True
        True
        >>> len('')
        0
        >>> len(' ')
        2
        """
    return len(string)
```