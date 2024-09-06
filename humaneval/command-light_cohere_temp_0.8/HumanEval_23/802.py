Here is a self-contained Python script that defines a function strlen that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: The length of the string in UTF-8 codepoints.
        Example a string provided as any argument is not checked, so empty strings or strings with invalid characters will not raise an error.
    """
    example:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```