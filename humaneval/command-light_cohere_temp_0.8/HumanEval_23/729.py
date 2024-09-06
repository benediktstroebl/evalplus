```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        5
        >>> strlen('123') == len('123')
        True
        >>> strlen('') == len('') + 1
        True
        """
    return len(string)
```