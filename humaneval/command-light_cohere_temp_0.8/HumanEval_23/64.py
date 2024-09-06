Here's a self-contained Python script that provides a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        4
        """
    return len(string)
```