```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen(' spaces')
        4
        >>> strlen('  ') == strlen('   '')
        True
        """
    return len(string)
```