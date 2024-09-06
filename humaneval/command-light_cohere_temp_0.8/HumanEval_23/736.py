```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('breaking news')
        6
        >>> strlen(' ')
        2
        >>> strlen('']
        2
        >>> strlen(' PixEffErC')
        10
        """
    return len(string)
```