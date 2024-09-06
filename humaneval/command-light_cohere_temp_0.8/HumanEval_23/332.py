```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        4
        >>> strlen('') | {'this is a test}
        0
        >>> len('abc')
        3
        """
    return len(string)
```