```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabcd')
        5
        >>> strlen('') | ""
        0
        >>> strlen('  ')
        1
        >>> strlen('   ')
        2
        """
    return len(string)
```