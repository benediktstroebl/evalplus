Here's a self-contained Python script that defines a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceclass: ValueError: expected str, got None
    """
    if not string: 
        raise ValueError('expected non empty string')
    return len(string)
```