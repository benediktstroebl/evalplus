Here is a self-contained Python script that defines a function `strlen` which calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    TypeError: unsupported operand type(string) for +() with int
    """
    return len(string)
```