Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        4
        >>> strlen('123') == len('123')
        True
        >>> strlen('') == len('')
        True
        """
    if not string:
        return 0
    return len(string)
```