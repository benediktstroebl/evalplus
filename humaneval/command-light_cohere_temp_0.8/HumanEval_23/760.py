Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>> strlen('this is a test')
    7
    >>> strlen('abc123')
    5
    """
    return len(string)
```