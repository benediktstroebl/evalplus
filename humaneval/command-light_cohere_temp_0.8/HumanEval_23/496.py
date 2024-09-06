Here is a Python script that provides a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    TypeError: Unbound variable 'string'
    """
    return len(string)
```  This code defines a function `strlen` that calculates the length of a given string.  It can be used as a drop-in replacement for the original code.