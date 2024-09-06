Here is a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    """ Returns the length of the given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('351')
    5
    >>> strlen('') == 0
    True
    """
    return len(string)
```