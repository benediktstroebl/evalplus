```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        4
        >>> strlen('') 
        Traceback (most recent call last):
            ValueError: 
            <string>: str(): invalid literal for identifier
        """
    if not string:
        return 0
    return len(string)
```