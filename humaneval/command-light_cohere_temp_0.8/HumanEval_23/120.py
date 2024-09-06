```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abot')
        4
        >>> strlen('   ')
        4
        >>> strlen('   a b a t')
        9
        """
    return len(string)
```