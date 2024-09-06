```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abc'}
        error: 'abc'}' is not str 
        """
    if not isinstance(string, str):
        raise TypeError("Input should be a string")
    return len(string)
```