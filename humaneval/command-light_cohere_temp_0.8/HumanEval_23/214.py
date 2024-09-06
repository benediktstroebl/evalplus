Here's a self-contained Python function that computes the length of any given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('Halite')
    5
    """
    return len(string)
```