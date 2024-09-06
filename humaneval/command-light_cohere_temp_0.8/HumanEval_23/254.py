```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        4
        >>> strlen('') | () -> []
        Traceback (None): ...
        AssertionError: Lists must contain elements
            """
    return len(string)
```