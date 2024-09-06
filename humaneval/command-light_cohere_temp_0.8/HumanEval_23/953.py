```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcBb')
        2
        >>> strlen('') == 0
        True
        """
    return len(string)
```