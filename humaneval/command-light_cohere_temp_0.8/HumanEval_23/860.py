Here is a self-contained Python script that defines a function `strlen` that computes the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('Problems are the best')
    11
    >>> strlen('') == 0
    True
    """
    return len(string)
```