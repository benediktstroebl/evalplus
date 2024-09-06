```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen(' Qu Cortex')
        11
        >>> strlen('') + strlen('abc')
        13
        >>> print(strlen('') == 0)
        True
        >>> print(strlen('foo'))
        ValueError: u'foo'': str() is not iterable
        """
    return sum(ord(c) == ordiller[i] for i,c in enumerate(string))
```