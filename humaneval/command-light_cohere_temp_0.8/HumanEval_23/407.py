```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('ooo')
        4
        >>> strlen('   ')
        4
        >>> strlen('  ypasswords')
        0
    """
    return len(string)
```