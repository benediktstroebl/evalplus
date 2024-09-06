Here's a self-contained Python script with a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abcxyz')
    5
    >>> strlen(' ')
    1
    """
    return len(string)
```