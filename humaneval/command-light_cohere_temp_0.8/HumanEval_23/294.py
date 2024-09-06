Here is a Python script with a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' ')
    4
    >>> strlen('1234')
    4
    >>> strlen(' Interior )  <ficcin> )
    11
    """
    return len(string)
```