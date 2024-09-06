```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abc bcd')
        4
        >>> strlen('')
        undefined TypeError: 'str.make()'(): str expected, int 
                """
    return len(string)
```