Here is a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc\n')
    3
    >>> strlen('abc123')
    3
    """
    return len(string)
```