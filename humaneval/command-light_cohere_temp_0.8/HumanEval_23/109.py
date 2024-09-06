```python
def strlen(string: str) -> int:
    """ Returns length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    TraceError: unsupported operand type(string) expected int, got str

    Attributes:
        - string (str): input string
    """
    if not string:  # empty string
        return 0
    return len(string)
```