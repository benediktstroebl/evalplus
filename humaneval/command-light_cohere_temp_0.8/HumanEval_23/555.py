```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcde')
        5
        >>> strlen(' ')
        1
        >>> strlen('   ')
        2
        >>> strlen('oint')
        3
        >>> strlen(' sutree')
        11
        """
    return len(string)
```