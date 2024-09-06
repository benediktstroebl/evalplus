Here's the self-contained Python function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>> strlen('ello world')
    13
    """
    return len(string)
```