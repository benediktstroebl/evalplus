Here is a Python script that contains a self-contained function that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    TypeError: 'arg' object does not support attribute 'strlen'
    """
    return len(string)
```