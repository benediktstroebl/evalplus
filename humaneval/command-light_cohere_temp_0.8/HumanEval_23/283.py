Here is a Python script that includes a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc') == 3
    True
    """
    return len(string)
```