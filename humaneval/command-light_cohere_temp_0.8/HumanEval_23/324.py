```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen(''''')
        4
        >>> strlen('   ')
        2
        >>> strlen('A')
        1
        >>> strlen(' HelLo')
        6
        """
    return len(string)
```