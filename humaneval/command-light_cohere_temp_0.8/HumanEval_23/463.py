```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('') 
        Traceback (most recent call last):
           File "<string>", line 20, in strlen()
           ...
           ValueError: unsupported operand type ('') expected
        """
    if not string:  # empty string has zero length
        return 0
    return len(string)
```