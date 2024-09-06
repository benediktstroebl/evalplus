```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcde')
        5
        >>> strlen('')
        Traceback (most recent call last):
            TypeError: 'argument' should be str, not None
        """
    return len(string)
```